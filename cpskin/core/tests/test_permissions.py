import unittest2 as unittest

from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING


class TestPermissions(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_portlets_permissions(self):
        portal = self.layer['portal']
        permission = 'Portlets: Manage portlets'
        roles = [r['name'] for r in portal.rolesOfPermission(permission) if r['selected']]
        self.assertEqual(roles, ['Editor', 'Manager', 'Portlets Manager', 'Site Administrator'])
