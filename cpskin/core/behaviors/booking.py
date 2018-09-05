# -*- coding: utf-8 -*-
from zope import schema

from cpskin.locales import CPSkinMessageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.interface import provider


@provider(IFormFieldProvider)
class IBooking(model.Schema):
    model.fieldset(
        'bookingview',
        label=_(
            u'Booking'),
        fields=(
            'booking_enable',
            'booking_price',
            'booking_url',
        ),
    )

    booking_enable = schema.Bool(
        title=_(u'Booking'),
        description=_(u'Is event booked'),  # noqa
        required=False,
        default=False,
    )

    booking_price = schema.TextLine(
        title=_(u'Tarriff'),
        description=u'',
        required=False,
    )

    booking_url = schema.URI(
        title=_(u'Ticketing'),
        required=False,
    )
