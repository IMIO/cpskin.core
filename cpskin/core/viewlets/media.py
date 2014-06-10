# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common
from plone import api
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from imio.media.browser import utils
import logging

logger = logging.getLogger('cpskin.core media viewlet')


class MediaViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('media.pt')

    @property
    def portal_catalog(self):
        return api.portal.get_tool(name='portal_catalog')

    def get_videos(self):
        videos = []
        video_brains = media_catalog_request('media_link',
                                             self.portal_catalog,
                                             2)
        for video_brain in video_brains:
            video = video_brain.getObject()
            state = api.content.get_state(video)
            if state.startswith("publish"):
                videos.append(utils.embed(video, self.request))
        return videos

    def get_albums(self):
        galleries = []
        gallery_brains = media_catalog_request('Folder',
                                               self.portal_catalog,
                                               5,
                                               hidden_tags=True)

        for gallery_brain in gallery_brains:
            if getattr(gallery_brain, 'hasContentLeadImage', False):
                gallery = gallery_brain.getObject()
                imagescale = self.context.unrestrictedTraverse(
                    gallery.getPhysicalPath() + ('@@images',))
                html = "<a href='{}'>".format(gallery.absolute_url())
                html += imagescale.scale('leadImage', width=300, height=300).tag()
                html += '</a>'

                galleries.append(html)
            else:
                logger.info("{} has no lead image".format(gallery_brain.getURL()))
        return galleries


def media_catalog_request(portal_type, portal_catalog, number, hidden_tags=False, view_name=None):
    hidden_keyword = api.portal.get_registry_record('cpskin.core.mediaviewlet')
    queryDict = {}
    queryDict['portal_type'] = portal_type
    queryDict['sort_on'] = 'created'
    if hidden_tags:
        queryDict['HiddenTags'] = hidden_keyword
    if view_name:
        # XXX create view_name index into plonetruegallery
        queryDict['view_name'] = view_name
    brains = portal_catalog(queryDict)[:number]
    if len(brains) > number:
        return brains[:number]
    return brains
