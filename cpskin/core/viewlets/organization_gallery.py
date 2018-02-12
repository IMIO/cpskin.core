# -*- coding: utf-8 -*-

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.layout.viewlets import common


class OrganizationGalleryViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('organization_gallery.pt')

    def available(self):
        return self.context.portal_type == 'organization'

    def get_photos(self):
        if not self.available():
            return []
        brains = api.content.find(
            context=self.context,
            portal_type='Image'
        )
        return [b.getObject() for b in brains]

    def image_url(self, obj, default_scale='preview'):
        url = ''
        images = obj.restrictedTraverse('@@images')
        image = images.scale('image', scale=default_scale)
        if image:
            url = image.url
        return url
