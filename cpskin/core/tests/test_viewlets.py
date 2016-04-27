import unittest

from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles


class TestViewlets(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_media_viewlet(self):
        view = self.portal.restrictedTraverse('opendata')
        links = view.get_links()
        self.assertEqual(len(links), 0)
