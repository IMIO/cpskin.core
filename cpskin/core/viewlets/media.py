# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common
from plone import api
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.plonetruegallery.utils import getGalleryAdapter


class MediaViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('media.pt')


    @property
    def portal_catalog(self):
        return api.portal.get_tool(name='portal_catalog')

    def get_videos(self):
        pass

    def get_albums(self):
        utils = getToolByName(self.context, 'plone_utils')
        utils.browserDefault(self.context)
        self.adapter = getGalleryAdapter(self.context, self.request)

