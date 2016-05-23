# -*- coding: utf-8 -*-
from cpskin.core.interfaces import ICPSkinCoreLayer
from cpskin.core.browser.folderview import configure_folderviews
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles
from zope.interface import directlyProvides

import unittest


class TestViews(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        directlyProvides(self.request, ICPSkinCoreLayer)

    def test_opendata_view(self):
        configure_folderviews(self.portal)
        self.portal.invokeFactory(
            'collective.directory.directory', 'directory1')
        view = self.portal.restrictedTraverse('opendata')
        links = view.get_links()
        self.assertEqual(len(links), 3)
