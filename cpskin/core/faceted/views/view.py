# -*- coding: utf-8 -*-
from collective.contact.core.browser.address import get_address
from cpskin.core.browser.contactdetails import ContactDetailsView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PreviewItem(ContactDetailsView):

    # def __init__(self, context, request):
    #     super(ContactDetailsView, self).__init__(context, request)
    #     self.contact_details = context

    def address(self):
        dict_address = get_address(self.context)
        template_path = 'address.pt'
        template = ViewPageTemplateFile(template_path)
        return template(self, dict_address)
