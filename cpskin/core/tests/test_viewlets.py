# -*- coding: utf-8 -*-
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import add_behavior
from cpskin.core.utils import add_keyword
from cpskin.core.utils import add_leadimage_from_file
from plone import api
from plone.app.testing import TEST_USER_ID, setRoles
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from zope.component import queryMultiAdapter
from zope.viewlet.interfaces import IViewletManager

import unittest


class TestViewlets(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_set_media_viewlet(self):
        view = getMultiAdapter((self.portal, self.request), name="media_activation")
        self.assertFalse('videos' in self.portal.keys())
        self.assertFalse(view.is_enabled)
        self.assertFalse(view.can_disable_media)

        view.enable_media()
        self.assertTrue(view.is_enabled)
        self.assertTrue(view.can_disable_media)
        self.assertTrue('videos' in self.portal.keys())

        view.disable_media()
        self.assertFalse(view.is_enabled)
        self.assertFalse(view.can_disable_media)
        self.assertTrue('videos' in self.portal.keys())

        view.enable_media()
        self.assertTrue(view.is_enabled)
        self.assertTrue(view.can_disable_media)
        self.assertTrue('videos' in self.portal.keys())

    def test_media_viewlet(self):
        keywords = ['album-a-la-une']
        view = getMultiAdapter((self.portal, self.request), name="media_activation")
        # create video collection used to viewlet
        view.enable_media()
        album_collection = self.portal.albums.index
        query = [
            {
                'i': 'hiddenTags',
                'o': 'plone.app.querystring.operation.selection.is',
                'v': keywords
            },
        ]

        # Set hiddenTags and leadimage behaviors
        add_behavior('Folder', 'cpskin.core.behaviors.metadata.IHiddenTags')
        add_behavior(
            'Folder',
            'plone.app.contenttypes.behaviors.leadimage.ILeadImage')

        album_collection.query = query
        album = api.content.create(container=self.portal, type="Folder", id="testalbum")

        # getting viewlet
        view = BrowserView(self.portal, self.request)
        manager_name = 'plone.belowcontent'
        manager = queryMultiAdapter((self.portal, self.request, view), IViewletManager, manager_name, default=None)
        self.assertIsNotNone(manager)
        manager.update()

        my_viewlet = [v for v in manager.viewlets if v.__name__ == 'cpskin.media']
        self.assertEqual(len(my_viewlet), 1)
        media_viewlet = my_viewlet[0]

        self.assertTrue(media_viewlet.available())
        self.assertEqual(
            media_viewlet.get_albums_collection().getPhysicalPath(),
            self.portal.albums.index.getPhysicalPath())
        self.assertEqual(len(media_viewlet.get_albums()), 0)

        # Set lead image to album folder
        add_leadimage_from_file(album, "cpskinlogo.png")
        add_keyword(album, 'hiddenTags', keywords)

        self.assertEqual(len(media_viewlet.get_albums()), 1)
