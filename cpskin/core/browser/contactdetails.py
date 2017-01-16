# -*- coding: utf-8 -*-
"""
cpskin.core
-----------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.Five import BrowserView
from collective.contact.core.browser.contactable import ContactDetails

import six

from cpskin.core import utils


class ContactDetailsView(BrowserView, ContactDetails):

    def __call__(self):
        self.update()
        return super(ContactDetailsView, self).__call__()

    @property
    def phones(self):
        phones = self.contact_details.get('phone', [])
        if isinstance(phones, six.string_types):
            phones = [phones]
        return [utils.format_phone(v) for v in phones]

    @property
    def cell_phones(self):
        cell_phones = self.contact_details.get('cell_phone', [])
        if isinstance(cell_phones, six.string_types):
            cell_phones = [cell_phones]
        return [utils.format_phone(v) for v in cell_phones]
