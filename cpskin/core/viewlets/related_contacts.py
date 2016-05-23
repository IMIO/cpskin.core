# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
import logging
logger = logging.getLogger('cpskin.core media viewlet')


class RelatedContactsViewlet(common.ViewletBase):

    def available(self):
        contacts = getattr(self.context, self.field, None)
        return bool(contacts)

    def get_contacts(self):
        contacts = []
        related_contacts = getattr(self.context, self.field, [])
        for related_contact in related_contacts:
            contacts.append(related_contact.to_object)
        return contacts


class AboveRelatedContactsViewlet(RelatedContactsViewlet):

    index = ViewPageTemplateFile('above_related_contacts.pt')
    field = 'aboveContentContact'


class BelowRelatedContactsViewlet(RelatedContactsViewlet):

    index = ViewPageTemplateFile('below_related_contacts.pt')
    field = 'belowContentContact'
