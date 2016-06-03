# -*- coding: utf-8 -*-
from cpskin.locales import CPSkinMessageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from plone.directives import form
from plone.supermodel import directives
from plone.supermodel import model
from z3c.form.browser.checkbox import SingleCheckBoxFieldWidget


@provider(IFormFieldProvider)
class ICpskinHomepage(model.Schema):
    model.fieldset(
        'homepage',
        label=_(
            u"Homepage, these settings are use only if this collection is marked has homepage content"),
        fields=(
            'slider_image_scale',
            'carousel_image_scale',
            'link_text',
            'use_keyword_homepage'
        ),
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
        description=_(u'This text will be visible on homepage'),
        default=_(u"Voir l'ensemble des"),
        required=True
    )

    form.widget('use_keyword_homepage', SingleCheckBoxFieldWidget)
    use_keyword_homepage = schema.Bool(
        title=_(u'Use keyword for homepage'),
        description=_(u'Use keyword(s) define in CPSkin settings.'),
        required=False,
        default=False,
    )
