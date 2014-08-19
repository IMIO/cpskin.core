# -*- coding: utf-8 -*-
from plone.supermodel import model
from plone.app.dexterity.behaviors.metadata import MetadataBase
from plone.autoform.interfaces import IFormFieldProvider
from cpskin.locales import CPSkinMessageFactory as _
from zope.interface import alsoProvides
from zope import schema


class IHiddenTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('hiddenTags',),
    )

    hiddenTags = schema.Tuple(
        title=_(u'label_hidden_tags', default=u'Hidden tags'),
        description=_(
            u'help_hidden_tags',
            default=u'Tags are commonly used for ad-hoc organization of ' +
                    u'content.'
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )


class IISearchTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('isearchTags',),
    )

    isearchTags = schema.Tuple(
        title=_(u'label_isearch_tags',  default=u'I Search Tags'),
        description=_(
            u'help_isearch_tags',
            default=u'I Search Tags are used for webmaster '
                    u'organization of content.'
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )

alsoProvides(IHiddenTags, IFormFieldProvider)
alsoProvides(IISearchTags, IFormFieldProvider)


class HiddenTags(MetadataBase):

    @property
    def hiddenTags(self):
        return self.context.hiddenTags

    @hiddenTags.setter
    def hiddenTags(self, value):
        values = []
        for index in value:
            if isinstance(index, unicode):
                values.append(index.encode('utf8'))
            else:
                values.append(index)
        self.context.hiddenTags = tuple(values)


class ISearchTags(MetadataBase):

    @property
    def isearchTags(self):
        return self.context.isearchTags

    @isearchTags.setter
    def isearchTags(self, value):
        values = []
        for index in value:
            if isinstance(index, unicode):
                values.append(index.encode('utf8'))
            else:
                values.append(index)
        self.context.isearchTags = tuple(values)
