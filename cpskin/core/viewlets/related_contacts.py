# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
import logging
logger = logging.getLogger('cpskin.core related contacts viewlet')


class RelatedContactsViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('related_contacts.pt')
    address_fields = ('street', 'number', 'zip_code', 'city')
    ignore_fields = ('title', )

    def available(self):
        contacts = getattr(self.context, self.field, None)
        return bool(contacts)

    @property
    def selected_fields(self):
        return getattr(self.context, self.selected, None)

    def get_contacts(self):
        contacts = []
        related_contacts = getattr(self.context, self.field, [])
        for related_contact in related_contacts:
            contacts.append(related_contact.to_object)
        return contacts

    def in_fields(self, field):
        return field in self.selected_fields

    def get_field(self, contact, field):
        # XXX find way to check if field is richetext or image or simple field
        if field == "activity":
            if getattr(contact, field, ''):
                text = getattr(contact, field).raw
                return text if text else ''
        if field in ['logo', 'photo']:
            if getattr(contact, field, ''):
                img = contact.restrictedTraverse('@@images')
                logo = img.scale(field)
                return logo.tag() if logo.tag() else ''
        return getattr(contact, field, '')

    def has_address(self):
        i = 0
        for address_field in self.address_fields:
            if address_field in self.selected_fields:
                i += 1
        return i == len(self.address_fields)

    def fields_without_address(self):
        fields = []
        for selected_field in self.selected_fields:
            if selected_field not in self.address_fields and \
                    selected_field not in self.ignore_fields:
                fields.append(selected_field)
        return fields

    def use_parent_address(self):
        pass


class AboveRelatedContactsViewlet(RelatedContactsViewlet):

    field = 'aboveContentContact'
    selected = 'aboveVisbileFields'


class BelowRelatedContactsViewlet(RelatedContactsViewlet):

    field = 'belowContentContact'
    selected = 'belowVisbileFields'
