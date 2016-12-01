# -*- coding: utf-8 -*-
from cpskin.locales import CPSkinMessageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from plone.directives import form
from z3c.form.browser.checkbox import CheckBoxFieldWidget


@provider(IFormFieldProvider)
class ICpskinIndexViewSettings(model.Schema):
    model.fieldset(
        'indexview',
        label=_(
            u"Index view"),
        fields=(
            'collection_image_scale',
            'slider_image_scale',
            'carousel_image_scale',
            'link_text',
            'index_view_keywords',
            'taxonomy_category',
            'item_count_homepage'
        ),
    )

    collection_image_scale = schema.Choice(
        title=_(u"Which image scale use for collections of index view"),
        description=_(u'Please select which fields should be visible.'),
        required=False,
        default='mini',
        vocabulary=u'plone.app.vocabularies.ImagesScales'
    )

    slider_image_scale = schema.Choice(
        title=_(u"Which image scale use for slider"),
        description=_(u''),
        required=True,
        default='slider',
        vocabulary=u'plone.app.vocabularies.ImagesScales'
    )

    carousel_image_scale = schema.Choice(
        title=_(u"Which image scale use for carousel"),
        description=_(u'Please select which fields should be visible.'),
        required=True,
        default='carousel',
        vocabulary=u'plone.app.vocabularies.ImagesScales'
    )

    link_text = schema.TextLine(
        title=_(u'Text for link to collection'),
        description=_(
            u'This text will be visible on index view for link to this collection'),
        default=_(u"Voir l'ensemble des"),
        required=True
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
        title=_(u"Which taxonomy id should be use to display category"),
        description=_(u'Please write which taxonomy id should be used.'),
        default=u'',
        required=False,
    )

    item_count_homepage = schema.Int(
        title=_(u'label_item_count_homepage', default=u'Item count for homepage'),
        description=_(u'Number of items that will show up in one homepage.'),
        required=False,
        default=8,
        min=1,
        max=30,
    )
