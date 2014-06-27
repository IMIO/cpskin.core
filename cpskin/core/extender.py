# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import public as atapi
from Products.Archetypes.interfaces import IBaseContent
from Products.CMFCore import permissions as zope_permissions

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
try:
    from plone.dexterity.utils import safe_unicode
    from plone.dexterity.utils import safe_utf8
except ImportError:
    # Compatibility with Plone 4.3.2 / plone.dexterity 2.1.3
    from cpskin.core.utils import safe_unicode
    from cpskin.core.utils import safe_utf8

from cpskin.locales import CPSkinMessageFactory as _

import permissions
from cpskin.core.interfaces import ICPSkinCoreLayer


class ExtensionIAmTagsField(ExtensionField, atapi.LinesField):
    """Derivate from Archetypes basic LinesField"""

    def set(self, instance, value, **kw):
        if isinstance(value, basestring):
            value = [value]
        instance.iamTags = tuple(safe_unicode(s.strip()) for s in value)
        instance.IAmTags = tuple(value)

    def get(self, instance, **kw):
        if getattr(instance, 'iamTags', None) is None:
            return ()
        return tuple(safe_utf8(s) for s in instance.iamTags)


class ExtensionISearchTagsField(ExtensionField, atapi.LinesField):
    """Derivate from Archetypes basic LinesField"""

    def set(self, instance, value, **kw):
        if isinstance(value, basestring):
            value = [value]
        instance.isearchTags = tuple(safe_unicode(s.strip()) for s in value)
        instance.ISearchTags = tuple(value)

    def get(self, instance, **kw):
        if getattr(instance, 'isearchTags', None) is None:
            return ()
        return tuple(safe_utf8(s) for s in instance.isearchTags)


class ExtensionHiddenTagsField(ExtensionField, atapi.LinesField):
    """Derivate from Archetypes basic LinesField"""

    def set(self, instance, value, **kw):
        if isinstance(value, basestring):
            value = [value]
        instance.hiddenTags = tuple(safe_unicode(s.strip()) for s in value)
        instance.HiddenTags = tuple(value)

    def get(self, instance, **kw):
        if getattr(instance, 'hiddenTags', None) is None:
            return ()
        return tuple(safe_utf8(s) for s in instance.hiddenTags)


class ContentExtender(object):
    adapts(IBaseContent)
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    layer = ICPSkinCoreLayer

    fields = [
        ExtensionIAmTagsField(
            'iamTags',
            multiValued=1,
            searchable=False,
            accessor='IAmTags',
            schemata="categorization",
            languageIndependent=True,
            widget=atapi.KeywordWidget(
                label=_(u'label_iam_tags', default=u'I Am Tags'),
                description=_(u'help_iam_tags',
                              default=u'I Am Tags are used for webmaster '
                                      u'organization of content.'),
            ),
            read_permission=zope_permissions.View,
            write_permission=permissions.CPSkinSiteAdministrator,
        ),
        ExtensionISearchTagsField(
            'isearchTags',
            multiValued=1,
            searchable=False,
            accessor='ISearchTags',
            schemata="categorization",
            languageIndependent=True,
            widget=atapi.KeywordWidget(
                label=_(u'label_isearch_tags', default=u'I Search Tags'),
                description=_(u'help_isearch_tags',
                              default=u'I Search Tags are used for webmaster '
                                      u'organization of content.'),
            ),
            read_permission=zope_permissions.View,
            write_permission=permissions.CPSkinSiteAdministrator,
        ),
        ExtensionHiddenTagsField(
            'hiddenTags',
            multiValued=1,
            searchable=False,
            accessor='HiddenTags',
            schemata="categorization",
            languageIndependent=True,
            widget=atapi.KeywordWidget(
                label=_(u'label_hidden_tags', default=u'Hidden Tags'),
                description=_(u'help_hidden_tags',
                              default=u'Hidden Tags are used for webmaster '
                                      u'organization of content.'),
            ),
            read_permission=zope_permissions.View,
            write_permission=permissions.CPSkinSiteAdministrator,
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        """
        Make sure that tags are just after subject in categorization schemata
        """
        if "subject" in schematas['categorization']:
            insertAfterFieldIndex = schematas['categorization'].index('subject')
        else:
            insertAfterFieldIndex = -1
        iAmTagsIndex = schematas['categorization'].index('iamTags')
        schematas['categorization'].insert(
                           insertAfterFieldIndex + 1,
                           schematas['categorization'].pop(iAmTagsIndex)
                           )
        iSearchTagsIndex = schematas['categorization'].index('isearchTags')
        schematas['categorization'].insert(
                           insertAfterFieldIndex + 2,
                           schematas['categorization'].pop(iSearchTagsIndex)
                           )
        hiddenTagsIndex = schematas['categorization'].index('hiddenTags')
        schematas['categorization'].insert(
                           insertAfterFieldIndex + 3,
                           schematas['categorization'].pop(hiddenTagsIndex)
                           )
        return schematas

    def getFields(self):
        return self.fields
