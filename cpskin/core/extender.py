# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import public as atapi
from Products.Archetypes.interfaces import IBaseContent
from Products.CMFCore import permissions

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender

from cpskin.locales import CPSkinMessageFactory as _

from cpskin.core.interfaces import ICPSkinCoreLayer


class ExtensionHiddenTagsField(ExtensionField, atapi.LinesField):
    """Derivate from Archetypes basic LinesField"""


class ContentExtender(object):
    adapts(IBaseContent)
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    layer = ICPSkinCoreLayer

    fields = [
        ExtensionHiddenTagsField(
            'hiddenTags',
            multiValued=1,
            searchable=False,
            schemata="categorization",
            languageIndependent=True,
            widget=atapi.KeywordWidget(
                label=_(u'label_hidden_tags', default=u'Hidden Tags'),
                description=_(u'help_hidden_tags',
                              default=u'Hidden Tags are used for webmaster '
                                      u'organization of content.'),
            ),
            read_permission=permissions.View,
            write_permission='Content rules: Manage rules',
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
