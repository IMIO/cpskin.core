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
        fields=('hiddentags',),
    )

    hiddentags = schema.Tuple(
        title=_(u'hidden_tags', default=u'Hidden tags'),
        description=_(
            u'help_hidden_tags',
            default=u'Tags are commonly used for ad-hoc organization of ' +
                    u'content.'
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )

alsoProvides(IHiddenTags, IFormFieldProvider)


class HiddenTags(MetadataBase):

    def _get_hiddentags(self):
        return self.context.subject

    def _set_hiddentags(self, value):
        self.context.subject = value
    hiddentags = property(_get_hiddentags, _set_hiddentags)
