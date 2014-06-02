# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import public as atapi
from Products.Archetypes.interfaces import IBaseContent
from Products.CMFCore import permissions as zope_permissions

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from plone.dexterity.utils import safe_unicode
from plone.dexterity.utils import safe_utf8

from cpskin.locales import CPSkinMessageFactory as _

import permissions
from cpskin.core.interfaces import ICPSkinCoreLayer


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
        schematas['categorization'] = ['subject', 'hiddenTags',
                                       'relatedItems', 'location', 'language']
        return schematas

    def getFields(self):
        return self.fields
