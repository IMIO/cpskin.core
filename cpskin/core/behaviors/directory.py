# -*- coding: utf-8 -*-

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider

from cpskin.locales import CPSkinMessageFactory as _


@provider(IFormFieldProvider)
class ICpskinDirectoryViewSettings(model.Schema):
    model.fieldset(
        'directoryview',
        label=_(
            u'Directory view'),
        fields=(
            'taxonomy_category',
            'organization_image_scale',
        ),
    )

    taxonomy_category = schema.TextLine(
        title=_(u'Which taxonomy id should be use to display category'),
        description=_(u'Please write which taxonomy id should be used.'),
        default=u'',
        required=False,
    )

    organization_image_scale = schema.Choice(
        title=_(u'Which image scale use for organizations preview in directory ?'),  # noqa
        description=_(u'Please select the scale.'),
        required=False,
        default='mini',
        vocabulary=u'plone.app.vocabularies.ImagesScales'
    )
