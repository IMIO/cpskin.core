# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.layout.viewlets import common
from zope.component import getMultiAdapter
from cpskin.core.interfaces import IAlbumCollection
from cpskin.core.interfaces import IVideoCollection
from imio.media.browser import utils

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

    def get_videos_collection(self):
        return self.get_collection(IVideoCollection)

    def get_videos(self):
        videos = []
        collection = self.get_videos_collection()
        if not collection:
            return None
        # limit = collection.getLimit()
        limit = 2
        brains = [b for b in collection.queryCatalog()][:limit]
        for brain in brains:
            video = brain.getObject()
            videos.append(utils.embed(video, self.request))
        return videos

    def get_albums_collection(self):
        return self.get_collection(IAlbumCollection)

    def get_albums(self):
        albums = []
        collection = self.get_albums_collection()
        if not collection:
            logger.info("{} has no album collection".format(self.context))
            return ""
        for gallery_brain in collection.queryCatalog():
            gallery = gallery_brain.getObject()
            imagescale = self.context.unrestrictedTraverse(
                gallery.getPhysicalPath() + ('@@images',))
            # AT
            if getattr(gallery_brain, 'hasContentLeadImage', False):
                html = "<a href='{}'>".format(gallery.absolute_url())
                html += imagescale.scale('leadImage', width=300, height=300).tag()
                html += '</a>'
                albums.append(html)
            # DX
            elif imagescale and not getattr(gallery_brain, 'hasContentLeadImage', False):
                html = "<a href='{}'>".format(gallery.absolute_url())
                html += imagescale.scale('image', width=300, height=300).tag()
                html += '</a>'
                albums.append(html)

            else:
                logger.info("{} has no lead image".format(gallery_brain.getURL()))
        limit = 5
        if 'visible_albums' in self.context.propertyIds():
            limit = self.context.getProperty('visible_albums')
        else:
            limit = api.portal.get_registry_record('cpskin.core.default_visible_albums')
        return albums[:limit]

    def get_collection(self, object_provide):
        queryDict = {}
        queryDict['object_provides'] = object_provide.__identifier__
        queryDict['path'] = {
            'query': '/'.join(self.context.getPhysicalPath()),
            'depth': 1
        }
        queryDict['sort_limit'] = 1
        brains = self.portal_catalog(queryDict)
        if len(brains) == 0:
            return None
        brain = brains[0]
        folder = brain.getObject()
        collection = getattr(folder, 'index', None)
        if not collection:
            return None
        return collection

    def get_one_album(self):
        galleries = self.get_albums()
        return galleries[:1]

    def get_four_albums(self):
        galleries = self.get_albums()
        return galleries[1:5]
