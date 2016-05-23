# -*- coding: utf-8 -*-
from collective.z3cform.keywordwidget.field import Keywords
from cpskin.locales import CPSkinMessageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.directives import form
from plone.supermodel import directives
from plone.supermodel import model
from z3c.form.browser.checkbox import SingleCheckBoxFieldWidget
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema
from zope.interface import alsoProvides
from zope.interface import provider


class IStandardTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('standardTags',),
    )

    form.widget(
        standardTags='collective.z3cform.keywordwidget.widget.KeywordFieldWidget')  # noqa
    standardTags = Keywords(
        title=_(u'label_standardTags', default=u'Standard Tags'),
        description=_(
            u'help_standard_tags',
            default=u'Standard Tags are used for webmaster '
                    u'organization of content.',
        ),
        required=False,
        # Automatically get the index in catalog by name
        index_name='standardTag',
    )


class IHiddenTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('hiddenTags',),
    )

    form.widget(
        hiddenTags='collective.z3cform.keywordwidget.widget.KeywordFieldWidget')  # noqa
    hiddenTags = Keywords(
        title=_(u'label_hidden_tags', default=u'Hidden Tags'),
        description=_(
            u'help_hidden_tags',
            default=u'Hidden Tags are used for webmaster '
                    u'organization of content.',
        ),
        required=False,
        # Automatically get the index in catalog by name
        index_name='hiddenTags',
    )


class IISearchTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('isearchTags',),
    )

    form.widget(
        isearchTags='collective.z3cform.keywordwidget.widget.KeywordFieldWidget')  # noqa
    isearchTags = Keywords(
        title=_(u'label_isearch_tags', default=u'I Search Tags'),
        description=_(
            u'help_isearch_tags',
            default=u'I Search Tags are used for webmaster '
                    u'organization of content.'
        ),
        required=False,
        index_name='isearchTags',
    )


class IIAmTags(model.Schema):
    model.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('iamTags',),
    )

    form.widget(
        iamTags='collective.z3cform.keywordwidget.widget.KeywordFieldWidget')
    iamTags = Keywords(
        title=_(u'label_iam_tags', default=u'I Am Tags'),
        description=_(
            u'help_iam_tags',
            default=u'I Am Tags are used for webmaster '
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


@provider(IFormFieldProvider)
class IRelatedContacts(model.Schema):
    directives.fieldset(
        'categorization',
        label=_(u'label_schema_categorization', default=u'Categorization'),
        fields=('aboveContentContact', 'aboveSeeTitle',
                'belowContentContact', 'belowSeeCoord'),
    )

    aboveContentContact = RelationList(
        title=u"Above content related contact",
        default=[],
        value_type=RelationChoice(
            title=_(u"Related"),
            source=ObjPathSourceBinder(
                portal_type=('person', 'organization')
            )
        ),
        required=False,
    )

    # form.widget('aboveSeeTitle', SingleCheckBoxFieldWidget)
    aboveSeeTitle = schema.Bool(
        title=_(u'See also title for above contacts'),
        description=_(
            u'By default, you see only description for related contacts located above content.'),  # noqa
        required=False,
        default=False,
    )

    belowContentContact = RelationList(
        title=u"Below content related contact",
        default=[],
        value_type=RelationChoice(
            title=_(u"Related"),
            source=ObjPathSourceBinder(
                portal_type=('person', 'organization')
            )
        ),
        required=False,
    )

    # form.widget('belowSeeCoord', SingleCheckBoxFieldWidget)
    belowSeeCoord = schema.Bool(
        title=_(u'See also coordinates for below contacts'),
        description=_(
            u'By default, you see only title for related contacts located below content.'),  # noqa
        required=False,
        default=False,
    )
