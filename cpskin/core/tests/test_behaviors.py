# -*- coding: utf-8 -*-
from cpskin.core.behaviors.metadata import IUseKeywordHomepage
from cpskin.core.interfaces import ICPSkinCoreLayer
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import queryUtility
from zope.interface import alsoProvides

import unittest


class TestBeahviors(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def _enable_behavior(self):
        fti = queryUtility(IDexterityFTI, name='Folder')
        behaviors = list(fti.behaviors)
        behaviors.append(IUseKeywordHomepage.__identifier__)
        fti._updateProperty('behaviors', tuple(behaviors))
        alsoProvides(self.request, IUseKeywordHomepage)

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        alsoProvides(self.request, ICPSkinCoreLayer)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'folder')
        self.folder = self.portal.folder

    def test_use_keyword_homepage(self):
        self._enable_behavior()
        useKeywordHomepage = getattr(self.folder, 'useKeywordHomepage')
        self.assertFalse(useKeywordHomepage)
