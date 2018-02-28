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
        ),
    )

    taxonomy_category = schema.TextLine(
        title=_(u'Which taxonomy id should be use to display category'),
        description=_(u'Please write which taxonomy id should be used.'),
        default=u'',
        required=False,
    )
