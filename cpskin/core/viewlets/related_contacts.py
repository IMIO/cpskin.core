# -*- coding: utf-8 -*-
from collective.contact.core.interfaces import IContactable
from cpskin.core.utils import format_phone
from plone.app.layout.viewlets import common
from plone.outputfilters.filters.resolveuid_and_caption import ResolveUIDAndCaptionFilter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging
logger = logging.getLogger('cpskin.core related contacts viewlet')


class RelatedContactsViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('related_contacts.pt')
    address_fields = ('street', 'number', 'zip_code', 'city',
                      'additional_address_details', 'region', 'country')
    coordinates_fields = ('phone', 'cell_phone', 'fax', 'email', 'im_handle',
                          'website')
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
        if field not in self.selected_fields:
            return ''
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
            if display.w.get('IScheduledContent.schedule', None):
                return display.w.get('IScheduledContent.schedule').render()
            else:
                return ''
        if field in ['phone', 'cell_phone', 'fax']:
            phones = getattr(contact, field, '')
            if not isinstance(phones, list):
                phones = [getattr(contact, field)]
            return [format_phone(phone) for phone in phones]
        return getattr(contact, field, '')


    def has_address(self):
        i = 0
        for address_field in self.address_fields:
            if address_field in self.selected_fields:
                i += 1
        return i >= 3

    def fields_without_address(self):
        fields = []
        for selected_field in self.selected_fields:
            if selected_field not in self.address_fields and \
                    selected_field not in self.ignore_fields and \
                    selected_field not in self.coordinates_fields:
                fields.append(selected_field)
        return fields

    def get_website(self, contact):
        website = self.get_field(contact, 'website')
        if website.startswith('http'):
            url = website
            website_name = website.replace('http://', '')
        else:
            url = 'http://{0}'.format(website)
            website_name = website
        html = ""
        html += '<a class="website" href="{0}" target="_blank">{1}</a>'.format(
            url, website_name)
        return html


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
