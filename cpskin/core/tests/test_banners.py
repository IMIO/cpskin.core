# -*- coding: utf-8 -*-
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.Five.browser import BrowserView
from zope.component import queryMultiAdapter
from zope.viewlet.interfaces import IViewletManager

import unittest


class TestBanners(unittest.TestCase):
    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        manager_name = 'plone.portaltop'
        view = BrowserView(self.portal, self.request)
        manager = queryMultiAdapter(
            (self.portal, self.request, view),
            IViewletManager,
            manager_name,
            default=None)
        manager.update()
        self.my_viewlet = [v for v in manager.viewlets
                           if v.__name__ == 'cpskin.banner'][0]

    def test_banner_without_folder(self):
        url = self.my_viewlet.getImageBannerUrl()
        self.assertEqual(url, u'http://nohost/plone/banner.jpg')

    def test_banner_with_folder_without_image(self):
        api.content.create(
            container=self.portal, type='Folder', id='banner')
        url = self.my_viewlet.getImageBannerUrl()
        self.assertEqual(url, u'http://nohost/plone/banner.jpg')

    def test_banner_with_folder_with_image(self):
        folder = api.content.create(
            container=self.portal, type='Folder', id='banner')
        api.content.create(
            container=folder, type='Image', id='image1.png')
        url = self.my_viewlet.getImageBannerUrl()
        self.assertEqual(url, u'http://nohost/plone/banner/image1.png')
