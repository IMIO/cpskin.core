# -*- coding: utf-8 -*-
from collective.contact.core.interfaces import IContactable
from plone.app.layout.viewlets import common
from plone.outputfilters.filters.resolveuid_and_caption import ResolveUIDAndCaptionFilter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
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

    def get_title(self, contact):
        if self.in_fields('title'):
            return u'<h4>{0}</h4>'.format(contact.title)
        else:
            return False

    def in_fields(self, field):
        return field in self.selected_fields

    def get_field(self, contact, field):
        if field in self.address_fields:
            contactable = IContactable(contact)
            details = contactable.get_contact_details()
            return details['address'].get(field)
        # XXX find way to check if field is richetext or image or simple field
        if field == 'activity':
            if getattr(contact, field, ''):
                text = getattr(contact, field).raw
                text = text.replace('http://resolveuid/', 'resolveuid/')
                parser = ResolveUIDAndCaptionFilter(contact)
                transform_text = parser(text)
                return transform_text if transform_text else ''
        if field in ['logo', 'photo']:
            if getattr(contact, field, ''):
                img = contact.restrictedTraverse('@@images')
                logo = img.scale(field)
                return logo.tag() if logo.tag() else ''
        if field == 'schedule':
            from plone.directives import dexterity
            display = dexterity.DisplayForm(contact, self.request)
            display.update()
            return display.w.get('IScheduledContent.schedule').render()
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


class AboveRelatedContactsViewlet(RelatedContactsViewlet):

    field = 'aboveContentContact'
    selected = 'aboveVisbileFields'


class BelowRelatedContactsViewlet(RelatedContactsViewlet):

    field = 'belowContentContact'
    selected = 'belowVisbileFields'

    def get_title(self, contact):
        if self.in_fields('title'):
            return u'<a href="{0}" target="_blank"><h4>{1}</h4></a>'.format(
                contact.absolute_url(),
                contact.title)
        else:
            return False
