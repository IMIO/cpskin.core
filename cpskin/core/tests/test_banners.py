# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from plone import api
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.namedfile.file import NamedBlobImage
from zope.component import queryMultiAdapter
from zope.viewlet.interfaces import IViewletManager

import os
import unittest


def dummy_image():
    filename = os.path.join(os.path.dirname(__file__), u'banner.png')
    return NamedBlobImage(
        data=open(filename, 'r').read(),
        filename=filename
    )


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
        url = self.my_viewlet.getBanner().get('url')
        self.assertTrue(url.startswith('http://nohost/plone/banner.jpg'))

    def test_banner_with_folder_without_image(self):
        api.content.create(
            container=self.portal, type='Folder', id='banner')
        url = self.my_viewlet.getBanner().get('url')
        self.assertTrue(url.startswith('http://nohost/plone/banner.jpg'))

    def test_banner_with_folder_with_image(self):
        folder = api.content.create(
            container=self.portal, type='Folder', id='banner')
        image = api.content.create(
            container=folder, type='Image', id='img1.png')
        image.image = dummy_image()
        url = self.my_viewlet.getBanner().get('url')
        self.assertTrue(url.startswith('http://nohost/plone/banner/img1.png'))
