import unittest

from plone.app.testing import applyProfile

from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.browser.folderview import configure_folderviews
from plone.app.testing import TEST_USER_ID, setRoles


class TestViews(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        configure_folderviews(self.portal)
        self.portal.invokeFactory('collective.directory.directory', 'directory1')

    def test_opendata_view(self):
        view = self.portal.restrictedTraverse('opendata')
        links = view.get_links()
        self.assertEqual(len(links), 4)
