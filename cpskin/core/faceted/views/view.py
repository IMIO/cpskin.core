# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.contact.core.browser.address import get_address
from cpskin.core.browser.contactdetails import ContactDetailsView


class PreviewItem(ContactDetailsView):

    def address(self):
        dict_address = get_address(self.context)
        template_path = 'address.pt'
        template = ViewPageTemplateFile(template_path)
        return template(self, dict_address)


class UtilsView(BrowserView):

    def image_url(self, obj, field, default_scale='preview'):
        url = ''
        images = obj.restrictedTraverse('@@images')
        if getattr(obj, field, False):
            image = images.scale(field, scale=default_scale)
            if image:
                url = image.url
        return url
