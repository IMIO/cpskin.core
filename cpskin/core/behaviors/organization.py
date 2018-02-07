# -*- coding: utf-8 -*-

from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedImage
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope.interface import provider

from cpskin.locales import CPSkinMessageFactory as _


@provider(IFormFieldProvider)
class IOrganizationImages(model.Schema):

    fieldset(
        'images',
        label=_(u'Images'),
        fields=['image1', 'image2'],
    )

    image1 = NamedImage(
        title=_("Image 1"),
        required=False,
    )

    image2 = NamedImage(
        title=_("Image 2"),
        required=False,
    )
