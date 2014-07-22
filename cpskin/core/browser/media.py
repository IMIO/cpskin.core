# -*- coding: utf-8 -*-
from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.Five.browser import BrowserView
from plone import api
from zope.component import getMultiAdapter
from zope.interface import alsoProvides
from zope.interface import implements
from zope.interface import noLongerProvides

from cpskin.locales import CPSkinMessageFactory as _

from cpskin.core.interfaces import (IMediaActivated,
                                    IAlbumCollection,
                                    IVideoCollection)
from cpskin.core.browser.interfaces import IMediaActivationView


class MediaActivationView(BrowserView):
    """
    Media activation helper view
    """
    implements(IMediaActivationView)

    def _redirect(self, msg=''):
        if self.request:
            if msg:
                api.portal.show_message(message=msg,
                                        request=self.request,
                                        type='info')
            self.request.response.redirect(self.context.absolute_url())
        return msg

    def _get_real_context(self):
        context = self.context
        plone_view = getMultiAdapter((context, self.request), name="plone")
        if plone_view.isDefaultPageInFolder():
            context = aq_parent(context)
        context = aq_inner(context)
        return context

    @property
    def is_enabled(self):
        # LATER : add caching here
        context = self._get_real_context()
        if IMediaActivated.providedBy(context):
            return True
        return False

    @property
    def can_enable_media(self):
        return not self.is_enabled

    @property
    def can_disable_media(self):
        context = self._get_real_context()
        return(IMediaActivated.providedBy(context))

    def enable_media(self):
        """ Enable the media """
        context = self._get_real_context()
        alsoProvides(context, IMediaActivated)
        catalog = api.portal.get_tool('portal_catalog')
        catalog.reindexObject(context)
        self._redirect(_(u'Multimedia viewlet enabled on content'))
        self.create_collections()

    def disable_media(self):
        """ Disable the media """
        context = self._get_real_context()
        noLongerProvides(context, IMediaActivated)
        catalog = api.portal.get_tool('portal_catalog')
        catalog.reindexObject(context)
        self._redirect(_(u'Multimedia viewlet disabled for content'))

    def create_collections(self):
        """ create videos and albums collections if not exists """
        catalog = api.portal.get_tool('portal_catalog')
        queryDict = {}
        queryDict['object_provides'] = IVideoCollection.__identifier__
        queryDict['path'] = {
            'query': '/'.join(self.context.getPhysicalPath()),
            'depth': 1
        }

        # --- Videos ---
        if not catalog(queryDict):
            video_folder = getattr(aq_base(self.context), 'videos', None)
            if not video_folder:
                video_folder = api.content.create(
                    container=self.context,
                    type='Folder',
                    id='video',
                    title=u"Vidéos"
                )

            alsoProvides(video_folder, IVideoCollection)
            video_folder.reindexObject()

            video_collection = getattr(aq_base(video_folder), 'index', None)
            if not video_collection:
                video_collection = api.content.create(
                    container=video_folder,
                    type='Collection',
                    id='index'
                )

            query = [
                {
                    'i': 'portal_type',
                    'o': 'plone.app.querystring.operation.selection.is',
                    'v': ['media_link']
                }, {
                    'i': 'review_state',
                    'o': 'plone.app.querystring.operation.selection.is',
                    'v': ['published_and_hidden', 'published_and_shown']
                }
            ]
            video_collection.query = query
            video_collection.sort_on = u'effective'
            video_collection.sort_reversed = True
            video_collection.setLayout('collection_oembed_view')

            if api.content.get_state(obj=video_folder) != 'published_and_hidden':
                api.content.transition(obj=video_folder, transition='publish_and_hide')

            if api.content.get_state(obj=video_collection) != 'published_and_hidden':
                api.content.transition(obj=video_collection, transition='publish_and_hide')

            video_folder.setDefaultPage('index')

        # --- Albums ---
        queryDict['object_provides'] = IAlbumCollection.__identifier__
        if not catalog(queryDict):
            album_folder = getattr(aq_base(self.context), 'albums', None)
            if not album_folder:
                album_folder = api.content.create(container=self.context,
                                                  type='Folder',
                                                  title=u"Albums")
            alsoProvides(album_folder, IAlbumCollection)
            album_folder.reindexObject()

            album_collection = getattr(aq_base(album_folder), 'index', None)
            if not album_collection:
                album_collection = api.content.create(
                    container=album_folder,
                    type='Collection',
                    id='index'
                )

            query = [
                {
                    'i': 'hiddenTags',
                    'o': 'plone.app.querystring.operation.selection.is',
                    'v': ['multimedia-a-la-une']
                }, {
                    'i': 'review_state',
                    'o': 'plone.app.querystring.operation.selection.is',
                    'v': ['published_and_hidden', 'published_and_shown']
                }
            ]
            # path = '/'.join(album_folder.getPhysicalPath())
            album_collection.query = query
            album_collection.limit = 3
            album_collection.sort_on = u'effective'
            album_collection.sort_reversed = True

            if api.content.get_state(obj=album_folder) != 'published_and_hidden':
                api.content.transition(obj=album_folder, transition='publish_and_hide')

            if api.content.get_state(obj=album_collection) != 'published_and_hidden':
                api.content.transition(obj=album_collection, transition='publish_and_hide')

            album_folder.setDefaultPage('index')
