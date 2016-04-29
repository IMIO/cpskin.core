# -*- coding: utf-8 -*-
from collective.z3cform.keywordwidget.field import Keywords
from cpskin.locales import CPSkinMessageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from plone.supermodel import directives
from plone.supermodel import model
from z3c.form.browser.checkbox import SingleCheckBoxFieldWidget
from zope import schema
from zope.interface import alsoProvides
from zope.interface import provider


class IStandardTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('standardTags',),
    )

    form.widget(standardTags='collective.z3cform.keywordwidget.widget.KeywordFieldWidget')
    standardTags = Keywords(
        title=_(u'label_standardTags', default=u'Standard Tags'),
        description=_(
            u'help_standard_tags',
            default=u'Standard Tags are used for webmaster '
                    u'organization of content.',
        ),
        required=False,
        # Automatically get the index in catalog by name
        index_name="standardTags",
    )


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


class IIAmTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('iamTags',),
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

alsoProvides(IStandardTags, IFormFieldProvider)
alsoProvides(IHiddenTags, IFormFieldProvider)
alsoProvides(IISearchTags, IFormFieldProvider)
alsoProvides(IIAmTags, IFormFieldProvider)


@provider(IFormFieldProvider)
class IUseKeywordHomepage(model.Schema):
    directives.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('useKeywordHomepage',),
    )

    form.widget('useKeywordHomepage', SingleCheckBoxFieldWidget)
    useKeywordHomepage = schema.Bool(
        title=_(u'Use keyword for homepage'),
        description=_(u'Use keyword(s) define in CPSkin settings.'),
        required=False,
        default=False,
    )
