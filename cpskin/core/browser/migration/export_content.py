from collective.exportimport.export_content import ExportContent
from Products.CMFCore.utils import getToolByName
from zope.interface import providedBy
from zope.component.interface import searchInterfaceUtilities

import logging
import re
import unicodedata

logger = logging.getLogger(__name__)
# 'grokcore.component.interfaces.IContext',
# 'plone.app.dexterity.behaviors.nextprevious.INextPreviousToggle',
# 'persistent.interfaces.IPersistent',
# 'plone.app.content.interfaces.INameFromTitle',
# 'collective.plonefinder.browser.interfaces.IFinderUploadCapable',
# 'plone.app.relationfield.interfaces.IDexterityHasRelations',
# 'plone.app.contenttypes.behaviors.leadimage.ILeadImage',
# 'OFS.interfaces.IObjectManager',
# 'collective.preventactions.browser.preventactions.IPreventActions',
# 'collective.plonetruegallery.interfaces.IGallery',
# 'Products.CMFCore.interfaces._content.IDynamicType',
# 'OFS.interfaces.ITraversable',
# 'plone.namedfile.interfaces.IImageScaleTraversable',
# 'plone.app.lockingbehavior.behaviors.ILocking',
# 'Products.CMFCore.interfaces._content.ICatalogableDublinCore',
# 'plone.dexterity.interfaces.IDexterityContainer',
# 'plone.folder.interfaces.IOrderableFolder',
# 'OFS.interfaces.IFolder',
# 'plone.dexterity.interfaces.IDexterityContent',
# 'Solgema.fullcalendar.interfaces.ISolgemaFullcalendarMarker',
# 'Products.CMFCore.interfaces._content.ICatalogAware',
# 'plone.uuid.interfaces.IAttributeUUID',
# 'Products.CMFCore.interfaces._content.IDublinCore',
# 'Products.CMFCore.interfaces._content.IOpaqueItemManager',
# 'plone.contentrules.engine.interfaces.IRuleAssignable',
# 'Products.CMFCore.interfaces._content.IContentish',
# 'Products.CMFCore.interfaces._content.IWorkflowAware',
# 'Products.CMFCore.interfaces._content.IFolderish',
# 'AccessControl.interfaces.IRoleManager',
# 'plone.app.multilingual.dx.interfaces.IDexterityTranslatable',
# 'Products.CMFPlone.interfaces.syndication.ISyndicatable',
# 'collective.behavior.richdescription.behavior.IRichDescription',
# 'eea.facetednavigation.subtypes.interfaces.IPossibleFacetedNavigable',
# 'zope.annotation.interfaces.IAttributeAnnotatable',
# 'Products.CMFDynamicViewFTI.interfaces.ISelectableBrowserDefault',
# 'OFS.interfaces.IItem',
# 'plone.app.contenttypes.interfaces.IFolder',
# 'collective.quickupload.interfaces.IQuickUploadCapable',
# 'cpskin.core.faceted.interfaces.ICPSkinPossibleFacetedNavigable',
# 'plone.portlets.interfaces.ILocalPortletAssignable'

INTERFACES_TO_KEEP = ["cpskin.minisite.interfaces.IMinisiteRoot"]

CONTACT_TYPES = ("organization", "person", "held_position")
RICHTEXT_PORTAL_TYPES = ("Document", "Procedure")


class CustomExportContent(ExportContent):

    def _slugify(self, text):
        """Convert text to a URL-friendly slug."""
        if isinstance(text, bytes):
            text = text.decode("utf-8", "ignore")
        text = unicodedata.normalize("NFKD", text)
        text = text.encode("ascii", "ignore").decode("ascii")
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"[\s_]+", "-", text)
        return text.strip("-")

    def _replace_contact_uid_links(self, html, catalog):
        """In an HTML string, replace resolveuid/[UID] hrefs that point to
        organization/person/position objects with annuaire/[slug]?u=[UID]."""
        if not html or "resolveuid" not in html.lower():
            return html

        def replacer(match):
            uid = match.group(1)
            brains = catalog(UID=uid)
            if brains and brains[0].portal_type in CONTACT_TYPES:
                if "Interface Entreprises" in brains[0].Title:
                    import pdb; pdb.set_trace()
                slug = self._slugify(brains[0].Title)
                return "fr/annuaire/{0}?u={1}".format(slug, uid)
            return match.group(0)

        return re.sub(r"resolveuid/([a-fA-F0-9-]+)", replacer, html, flags=re.IGNORECASE)

    def _process_link_contact_remoteurl(self, item, obj):
        """For Link: if remoteUrl is a resolveuid pointing to a contact,
        replace it with the annuaire slugged URL."""
        if obj.portal_type != "Link":
            return
        remote_url = item.get("remoteUrl", "")
        if not remote_url or "resolveuid" not in remote_url.lower():
            return
        match = re.search(r"resolveuid/([a-fA-F0-9-]+)", remote_url, re.IGNORECASE)
        if not match:
            return
        uid = match.group(1)
        catalog = getToolByName(obj, "portal_catalog")
        brains = catalog(UID=uid)
        if brains and brains[0].portal_type in CONTACT_TYPES:
            slug = self._slugify(brains[0].Title)
            item["remoteUrl"] = "fr/annuaire/{0}?u={1}".format(slug, uid)

    def _process_richtext_contact_links(self, item, obj):
        """For Document/Procedure: scan all richtext fields and replace
        resolveuid links pointing to contacts with annuaire slugged URLs."""
        if obj.portal_type not in RICHTEXT_PORTAL_TYPES:
            return
        catalog = getToolByName(obj, "portal_catalog")
        for key, value in item.items():
            if isinstance(value, dict) and "data" in value:
                # Richtext field serialized as {"content-type": ..., "data": ..., "encoding": ...}
                value["data"] = self._replace_contact_uid_links(value["data"], catalog)
            elif isinstance(value, str) and "resolveuid" in value.lower():
                item[key] = self._replace_contact_uid_links(value, catalog)

    def zmi_provided(self, obj):
        provided = providedBy(obj)
        for name, iface in searchInterfaceUtilities(obj):
            if iface in provided:
                yield iface

    def global_obj_hook(self, obj):
        """Inspect the content item before serialization data."""
        __interfaces = [
            iface.__identifier__
            for iface in self.zmi_provided(obj)
            if iface.__identifier__ in INTERFACES_TO_KEEP
        ]
        setattr(obj, "_cpskin_interfaces", __interfaces)
        return obj

    def global_dict_hook(self, item, obj):
        """Use this to modify or skip the serialized data.
        Return None if you want to skip this particular object.
        """
        item["aboveContentContact"] = self._extract_contact_dicts(item,
            obj, "aboveContentContact", label="ABOVE"
        )

        item["belowContentContact"] = self._extract_contact_dicts(item,
            obj, "belowContentContact", label="BELOW"
        )
        if hasattr(obj, "see_map"):
            item["see_map"] = getattr(obj, "see_map")
        if hasattr(obj, "_cpskin_interfaces"):
            item["_cpskin_interfaces"] = getattr(obj, "_cpskin_interfaces")
        if hasattr(obj, "getDefaultPage") and obj.getDefaultPage() is not None:
            print("Ooooooh une default page :-) !!")
            item["_cpskin_default_page"] = obj.getDefaultPage()
        self._process_richtext_contact_links(item, obj)
        self._process_link_contact_remoteurl(item, obj)
        return item

    # activity_min_len = 700 >> deprecated
    # Finalement, on reprend systematiquement ce qu'il y a dans activity
    # car ce qui compte c'est de recuperer ce texte de facon structuree
    def _extract_contact_dicts(self, item, obj, field_name, label="", activity_min_len=0):
        if not hasattr(obj, field_name):
            return []
        related_contacts = getattr(obj, field_name) or []
        result = []

        for rel in related_contacts:
            try:
                contact_target = rel.to_object
                if contact_target is None:
                    raise ValueError("Relation target is None (to_object)")
                wftool = getToolByName(contact_target, 'portal_workflow')
                state = wftool.getInfoFor(contact_target, 'review_state')
                if state != "private":
                    d = {
                        "uid": contact_target.UID(),
                        "id": contact_target.getId(),
                        "title": contact_target.Title(),
                        "portal_type": getattr(contact_target, "portal_type", None),
                    }

                    activity_output = getattr(getattr(contact_target, "activity", None), "output", None)
                    if activity_output:
                        clean_activity_text = re.sub(r'[\r\n\t]', '', activity_output)
                        if len(clean_activity_text) > activity_min_len:
                            d["activity"] = clean_activity_text

                    result.append(d)
            except Exception as e:
                logger.warning(
                    "=> %s contact is broken for %s (%s)",
                    label or field_name,
                    obj.absolute_url(),
                    e,
                )

        return result
