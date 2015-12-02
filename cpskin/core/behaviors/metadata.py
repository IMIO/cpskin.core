# -*- coding: utf-8 -*-
from zope.interface import alsoProvides

from collective.z3cform.keywordwidget.field import Keywords
from plone.supermodel import model
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form

from cpskin.locales import CPSkinMessageFactory as _


class IHiddenTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('hiddenTags',),
    )

    form.widget(hiddenTags='collective.z3cform.keywordwidget.widget.KeywordFieldWidget')
    hiddenTags = Keywords(
        title=_(u'label_hidden_tags', default=u'Hidden Tags'),
        description=_(
            u'help_hidden_tags',
            default=u'Hidden Tags are used for webmaster '
                    u'organization of content.',
        ),
        required=False,
        # Automatically get the index in catalog by name
        index_name="hiddenTags",
    )


class IISearchTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('isearchTags',),
    )

    form.widget(isearchTags='collective.z3cform.keywordwidget.widget.KeywordFieldWidget')
    isearchTags = Keywords(
        title=_(u'label_isearch_tags', default=u'I Search Tags'),
        description=_(
            u'help_isearch_tags',
            default=u'I Search Tags are used for webmaster '
                    u'organization of content.'
        ),
        required=False,
        index_name="isearchTags",
    )


class IAmTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('iamtags',),
    )

    form.widget(iamTags='collective.z3cform.keywordwidget.widget.KeywordFieldWidget')
    iamTags = Keywords(
        title=_(u'label_iam_tags', default=u'I am Tags'),
        description=_(
            u'help_iam_tags',
            default=u'I am Tags are used for webmaster '
                    u'organization of content.',
        ),
        required=False,
        # Automatically get the index in catalog by name
        index_name="iamTags",
    )

alsoProvides(IHiddenTags, IFormFieldProvider)
alsoProvides(IISearchTags, IFormFieldProvider)
alsoProvides(IAmTags, IFormFieldProvider)
