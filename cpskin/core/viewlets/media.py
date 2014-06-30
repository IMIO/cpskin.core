# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from imio.media.browser import utils
from plone import api
from plone.app.layout.viewlets import common
from zope.component import getMultiAdapter

import logging
logger = logging.getLogger('cpskin.core media viewlet')


class MediaViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('media.pt')

    def available(self):
        context = self.context
        media_view = getMultiAdapter((context, self.request),
                                      name="media_activation")
        return media_view.is_enabled
    @property
    def portal_catalog(self):
        return api.portal.get_tool(name='portal_catalog')

    def get_videos(self):
        videos = []
        video_brains = media_catalog_request('media_link',
                                             self.context,
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
                                               self.context,
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

    def get_one_album(self):
        galleries = self.get_albums()
        return galleries[:1]

    def get_four_albums(self):
        galleries = self.get_albums()
        return galleries[1:5]


def media_catalog_request(
        portal_type,
        context,
        portal_catalog,
        number,
        hidden_tags=False,
        view_name=None):
    hidden_keyword = api.portal.get_registry_record('cpskin.core.mediaviewlet')
    queryDict = {}
    queryDict['portal_type'] = portal_type
    queryDict['sort_on'] = 'effective'
    queryDict['sort_order'] = 'reverse'
    queryDict['path'] = {'query': '/'.join(context.getPhysicalPath()),
                         'depth': 5}
    if hidden_tags:
        queryDict['HiddenTags'] = hidden_keyword
    if view_name:
        # XXX create view_name index into plonetruegallery
        queryDict['view_name'] = view_name
    brains = portal_catalog(queryDict)[:number]
    if len(brains) > number:
        return brains[:number]
    return brains
