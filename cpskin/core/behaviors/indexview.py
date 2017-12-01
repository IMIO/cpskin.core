# -*- coding: utf-8 -*-
from cpskin.core.vocabulary import index_view_display_type
from cpskin.locales import CPSkinMessageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ICpskinIndexViewSettings(model.Schema):
    model.fieldset(
        'indexview',
        label=_(
            u'Index view'),
        fields=(
            'display_type',
            'minimum_items_in_slider',
            'maximum_items_in_slider',
            'collection_image_scale',
            'slider_image_scale',
            'carousel_image_scale',
            'link_text',
            'index_view_keywords',
            'taxonomy_category',
            'item_count_homepage',
            'hide_title',
            'hide_see_all_link',
            'hide_date',
            'show_day_and_month',
            'show_descriptions',
            'use_new_template',
        ),
    )

    display_type = schema.Choice(
        title=_(u'Collection display type'),
        description=_(u'How do you want to display this collection on index view ?'),  # noqa
        required=False,
        vocabulary=index_view_display_type
    )

    minimum_items_in_slider = schema.Int(
        title=_(u'Minimum number of items in slider'),
        description=_(u'How many items do you want to see at least in slider (used only for "Slider with elements count choice" display type) ?'),  # noqa
        required=True,
        default=2,
        min=1,
        max=5,
    )

    maximum_items_in_slider = schema.Int(
        title=_(u'Maximum number of items in slider'),
        description=_(u'How many items do you want to see at most in slider (used only for "Slider with elements count choice" display type) ?'),  # noqa
        required=True,
        default=4,
        min=1,
        max=7,
    )

    collection_image_scale = schema.Choice(
        title=_(u'Which image scale use for collections of index view'),
        description=_(u'Please select which fields should be visible.'),
        required=False,
        default='collection',
        vocabulary=u'plone.app.vocabularies.ImagesScales'
    )

    slider_image_scale = schema.Choice(
        title=_(u'Which image scale use for slider'),
        description=_(u''),
        required=True,
        default='slider',
        vocabulary=u'plone.app.vocabularies.ImagesScales'
    )

    carousel_image_scale = schema.Choice(
        title=_(u'Which image scale use for carousel'),
        description=_(u'Please select which fields should be visible.'),
        required=True,
        default='carousel',
        vocabulary=u'plone.app.vocabularies.ImagesScales'
    )

    link_text = schema.TextLine(
        title=_(u'Text for link to collection'),
        description=_(
            u'This text will be visible on index view for link to this collection'),  # noqa
        default=_(u''),
        required=False
    )

    form.widget('index_view_keywords', CheckBoxFieldWidget)
    index_view_keywords = schema.List(
        title=_(u'Hidden keywords'),
        description=_(
            u'Please select which hidden keywords is use by collections for \
            index view.'),
        required=False,
        value_type=schema.Choice(
            vocabulary=u'cpskin.core.vocabularies.hiddenTags'
        )
    )

    taxonomy_category = schema.TextLine(
        title=_(u'Which taxonomy id should be use to display category'),
        description=_(u'Please write which taxonomy id should be used.'),
        default=u'',
        required=False,
    )

    item_count_homepage = schema.Int(
        title=_(
            u'label_item_count_homepage',
            default=u'Item count for homepage'),
        description=_(u'Number of items that will show up in one homepage.'),
        required=False,
        default=8,
        min=1,
        max=30,
    )

    hide_title = schema.Bool(
        title=_(u'Hide title'),
        description=_(u'Do you want to hide title on index view ?'),
        required=False,
        default=False
    )

    hide_see_all_link = schema.Bool(
        title=_(u'Hide see all link'),
        description=_(u'Do you want to hide see all link on index view ?'),
        required=False,
        default=False
    )

    hide_date = schema.Bool(
        title=_(u'Hide date'),
        description=_(u'Do you want to hide date on index view ?'),
        required=False,
        default=False
    )

    show_day_and_month = schema.Bool(
        title=_(u'Show day and month'),
        description=_(
            u'Do you want to show day and month instead of lead image on index view ?'),  # noqa
        required=False,
        default=False
    )

    show_descriptions = schema.Bool(
        title=_(u'Show items descriptions'),
        description=_(
            u'Do you want to show items descriptions on index view ?'),
        required=False,
        default=False
    )

    use_new_template = schema.Bool(
        title=_(u'Use new template'),
        description=_(u'Do you want to use the new (experimental) template ?'),
        required=False,
        default=False
    )
