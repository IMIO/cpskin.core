# -*- coding: utf-8 -*-
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import set_plonecustom_last
from plone import api

import unittest


class TestTools(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_plonecustom_to_last(self):
        portal_css = api.portal.get_tool('portal_css')
        resources = list(portal_css.resources)
        self.assertFalse(resources[-1].getId() == 'ploneCustom.css')
        set_plonecustom_last()
        resources = list(portal_css.resources)
        self.assertTrue(resources[-1].getId() == 'ploneCustom.css')
