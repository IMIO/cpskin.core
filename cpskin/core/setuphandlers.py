# -*- coding: utf-8 -*-
import os
import logging
from zope.component import getAdapter
from zope.component import getUtility
from zope.component import queryMultiAdapter
from zope.interface import noLongerProvides
from plone import api
from plone.dexterity.interfaces import IDexterityFTI
from plone.registry import field, Record
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import bodyfinder
from plone.app.controlpanel.security import ISecuritySchema

from cpskin.locales import CPSkinMessageFactory as _

logger = logging.getLogger('cpskin.core')


def installCore(context):
    if context.readDataFile('cpskin.core-default.txt') is None:
        return

    logger.info('Installing')
    portal = context.getSite()

    # Rename events and news
    ChangeCollectionsIds(portal)

    # Add the MaildropHost if possible
    addMaildropHost(portal)

    # Add catalog indexes
    addCatalogIndexes(portal)

    # Create default banner image
    addImageFromFile(portal, 'banner.jpg')

    # Create default visuel image
    addImageFromFile(portal, 'visuel.png')

    # Create default logo
    addImageFromFile(portal, 'cpskinlogo.png')

    # Add HiddenTags behavior to collective.directory types
    addBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IHiddenTags',
        'collective.directory.directory')
    addBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IISearchTags',
        'collective.directory.directory')

    addBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IHiddenTags',
        'collective.directory.category')
    addBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IHiddenTags',
        'collective.directory.card')
    addBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IISearchTags',
        'collective.directory.card')

    # Create footer static page
    footer_name = 'footer-static'
    if not portal.hasObject(footer_name):
        footer = api.content.create(type='Document',
                                    title=footer_name,
                                    container=portal)
        footer.setTitle(footer_name)

    configCollectiveQucikupload(portal)

    addLoadPageMenuToRegistry()


def configureMembers(context):
    if context.readDataFile('cpskin.core-membersconfig.txt') is None:
        return

    logger.info('Configuring members')
    portal = context.getSite()

    pm = getToolByName(portal, 'portal_membership')
    if not pm.getMemberareaCreationFlag():
        pm.setMemberareaCreationFlag()

    # Add a citizen group
    api.group.create('citizens', title='Citizens')

    security = getAdapter(portal, ISecuritySchema)
    # Activate Members folders
    security.set_enable_user_folders(True)
    # Activate anonymous registration
    security.set_enable_self_reg(True)

    # Clean user interface
    members = portal['Members']
    members.manage_permission('Sharing page: Delegate roles',
                              ('Manager', 'Site Administrator', 'Reviewer'),
                              acquire=0)
    members.manage_permission('Modify view template',
                              ('Manager', 'Site Administrator', 'Reviewer'),
                              acquire=0)
    members.manage_permission('Review portal content',
                              ('Manager', 'Site Administrator', 'Reviewer'),
                              acquire=0)
    members.manage_permission('Modify constrain types',
                              ('Manager', 'Site Administrator', 'Reviewer'),
                              acquire=0)

    if not members.hasObject('help-page'):
        # add Members help page
        helpPage = api.content.create(container=members, type='Document',
                                      id='help-page',
                                      title="Bienvenue dans l'espace citoyen")
        # needed because of https://github.com/plone/plone.api/issues/99
        helpPage.setTitle("Bienvenue dans l'espace citoyen")
        setPageText(portal, helpPage, 'cpskin-helppage-setup')
        members.setDefaultPage('help-page')
        members.setExcludeFromNav(True)
        # we set locally allowed types at the first configuration
        members.setConstrainTypesMode(1)
        members.setLocallyAllowedTypes(['Event'])
        members.setImmediatelyAddableTypes(['Event'])


def uninstallCore(context):
    if context.readDataFile('cpskin.core-uninstall.txt') is None:
        return

    logger.info('Uninstalling')
    portal = context.getSite()

    # Remove banner image
    if portal.hasObject('banner.jpg'):
        api.content.delete(obj=portal['banner.jpg'])

    # Remove visuel image
    if portal.hasObject('visuel.png'):
        api.content.delete(obj=portal['visuel.png'])

    # Remove default logo
    if portal.hasObject('cpskinlogo.png'):
        api.content.delete(obj=portal['cpskinlogo.png'])

    # Remove footer static
    if portal.hasObject('footer-static'):
        api.content.delete(obj=portal['footer-static'])

    # Remove dexterity behaviors
    removeBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IHiddenTags',
        'collective.directory.directory')
    removeBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IISearchTags',
        'collective.directory.directory')

    removeBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IHiddenTags',
        'collective.directory.category')
    removeBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IHiddenTags',
        'collective.directory.card')
    removeBehavior(
        portal,
        'cpskin.core.behaviors.metadata.IISearchTags',
        'collective.directory.card')

    unregisterProvidesInterfaces(portal)


def unregisterProvidesInterfaces(portal):
    from cpskin.core.interfaces import (
        IBannerActivated,
        IMediaActivated,
        IAlbumCollection,
        IVideoCollection
    )

    interfaces = [IBannerActivated,
                  IMediaActivated,
                  IAlbumCollection,
                  IVideoCollection]
    for interface in interfaces:
        catalog = getToolByName(portal, 'portal_catalog')
        brains = catalog({
            "object_provides": interface.__identifier__,
        })
        for brain in brains:
            obj = brain.getObject()
            noLongerProvides(obj, interface)
            obj.reindexObject()


def setPageText(portal, page, viewName):
    """
    Sets text of a Plone document if it exists and reindex the document
    The text is coming from a browser view template <body> tag
    """
    if page is None:
        return
    request = getattr(portal, 'REQUEST', None)
    if request is not None:
        view = queryMultiAdapter((portal, request), name=viewName)
        if view is not None:
            text = bodyfinder(view.index()).strip()
            page.setText(text, mimetype='text/html')
            page.reindexObject()


def addMaildropHost(self):
    """
     Add a MaildropHost if Products.MaildropHost is available...
     If MaildropHost exist, PloneGazette will use it to send mails.
     This will avoid duplicate emails send as reported by
    """
    portal = getToolByName(self, 'portal_url').getPortalObject()
    if not hasattr(portal, "MaildropHost"):
        try:
            portal.manage_addProduct['MaildropHost'].manage_addMaildropHost('MaildropHost', title='MaildropHost')
        except AttributeError:
            # if MaildropHost is not available, we pass...
            pass


def addCatalogIndexes(portal):
    """
    Method to add our wanted indexes to the portal_catalog.
    We couldn't do it in the profile directly, see :
        http://maurits.vanrees.org/weblog/archive/2009/12/catalog
    """
    catalog = getToolByName(portal, 'portal_catalog')
    indexes = catalog.indexes()
    wanted = (('standardTags', 'KeywordIndex'),
              ('iamTags', 'KeywordIndex'),
              ('isearchTags', 'KeywordIndex'),
              ('hiddenTags', 'KeywordIndex'))
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def ChangeCollectionsIds(portal):
    # required : topic object need a _p_jar for rename
    import transaction
    transaction.savepoint()
    if portal.hasObject('news'):
        news = portal['news']
        if news.hasObject('aggregator'):
            news['aggregator'].setExcludeFromNav(True)
            api.content.rename(obj=news['aggregator'], new_id='index')
        news.setExcludeFromNav(True)
        api.content.rename(obj=news, new_id='actualites')
    if portal.hasObject('events'):
        events = portal['events']
        if events.hasObject('aggregator'):
            events['aggregator'].setExcludeFromNav(True)
            api.content.rename(obj=events['aggregator'], new_id='index')
        events.setExcludeFromNav(True)
        api.content.rename(obj=events, new_id='evenements')


def addImageFromFile(portal, fileName):
    dataPath = os.path.join(os.path.dirname(__file__), 'data')
    filePath = os.path.join(dataPath, fileName)
    fd = open(filePath, 'rb')
    if not portal.hasObject(fileName):
        image = api.content.create(type='Image',
                                   title=fileName,
                                   container=portal,
                                   file=fd)
        image.setTitle(fileName)
        image.reindexObject()
    fd.close()


def addBehavior(portal, behavior, name):
    """
    Add HiddenTags behavior to dexterity named type
    """
    fti = getUtility(IDexterityFTI, name=name)

    behaviors = list(fti.behaviors)

    if behavior not in behaviors:
        behaviors.append(behavior)
        fti.behaviors = behaviors


def removeBehavior(portal, behavior, name):
    """
    Remove HiddenTags behavior dexterity named type
    """
    fti = getUtility(IDexterityFTI, name=name)

    behaviors = list(fti.behaviors)

    if behavior in behaviors:
        behaviors.remove(behavior)
        fti.behaviors = behaviors


def configCollectiveQucikupload(portal):
    ptool = getToolByName(portal, 'portal_properties')
    qu_props = ptool.get('quickupload_properties')
    if not qu_props.hasProperty('show_upload_action'):
        qu_props._setProperty('show_upload_action', True, 'boolean')
    else:
        qu_props.show_upload_action = True


def addLoadPageMenuToRegistry():
    registry = getUtility(IRegistry)

    logger.info("Adding cpskin.core.interfaces.ICPSkinSettings.load_page_menu to registry")
    record = Record(field.Bool(title=_(u"Load page menu"),
                               description=_(u"Is level 1 menu load page at click?"),
                               required=False,
                               default=False),
                    value=False)

    registry.records['cpskin.core.interfaces.ICPSkinSettings.load_page_menu'] = record
