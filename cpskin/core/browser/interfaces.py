# -*- coding: utf-8 -*-
from zope import schema
from zope.interface import Interface

from Products.CMFDefault.formlib.schema import EmailLine

from cpskin.locales import CPSkinMessageFactory as _


class ISendToManagerForm(Interface):
    """ Interface for describing the 'sendtomanager' form """

    send_from_address = EmailLine(
        title=_(u'label_send_from',
                default=u'From'),
        description=_(u'help_send_from',
                      default=u'Your email address.'),
        required=True
    )

    comment = schema.Text(
        title=_(u'label_comment',
                default=u'Change request'),
        description=_(u'help_comment',
                      default=u'Report an error or missing information.'),
        required=False
    )
