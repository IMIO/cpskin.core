import unittest2 as unittest

from plone.app.testing import applyProfile

from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING


class TestProfiles(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_uninstall(self):
        applyProfile(self.portal, 'cpskin.core:uninstall')

    def test_reinstall(self):
        applyProfile(self.portal, 'cpskin.core:uninstall')
        applyProfile(self.portal, 'cpskin.core:default')

    def test_uninstall_with_members(self):
        applyProfile(self.portal, 'cpskin.core:members-configuration')
        applyProfile(self.portal, 'cpskin.core:uninstall')
