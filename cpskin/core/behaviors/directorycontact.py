# -*- coding: utf-8 -*-
"""
cpskin.core
-----------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from collective.contact.core import _ as CCMF
from collective.contact.core.behaviors import IContactDetails
from collective.contact.core.behaviors import validatePhone
from cpskin.core.browser.widget import multiline_field_widget
from cpskin.locales import CPSkinMessageFactory as _
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from zope.interface import provider


def validate_phones(values):
    for value in values:
        validatePhone(value)
    return True


@provider(IFormFieldProvider)
class IDirectoryContactDetails(IContactDetails):

    form.widget(phone=multiline_field_widget)
    phone = schema.List(
        title=_(u'Phones'),
        required=False,
        constraint=validate_phones,
    )

    form.widget(cell_phone=multiline_field_widget)
    cell_phone = schema.List(
        title=CCMF(u'Cell phone'),
        required=False,
    )
