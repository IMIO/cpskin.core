# -*- coding: utf-8 -*-
from cpskin.core.behaviors.metadata import IRelatedContacts
from cpskin.core.behaviors.metadata import IUseKeywordHomepage
from cpskin.core.interfaces import ICPSkinCoreLayer
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import add_behavior
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import queryUtility
from zope.interface import alsoProvides

import unittest


class TestBeahviors(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        alsoProvides(self.request, ICPSkinCoreLayer)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'folder')
        self.folder = self.portal.folder
        self.portal.invokeFactory('Document', 'document')
        self.document = self.portal.document

    def test_use_keyword_homepage(self):
        add_behavior('Folder', IUseKeywordHomepage.__identifier__)
        useKeywordHomepage = getattr(self.folder, 'useKeywordHomepage')
        self.assertFalse(useKeywordHomepage)

    def test_related_contacts(self):
        add_behavior('Document', IRelatedContacts.__identifier__)
        aboveContentContact = getattr(self.document, 'aboveContentContact')
        self.assertEqual(aboveContentContact, [])
        belowContentContact = getattr(self.document, 'belowContentContact')
        self.assertFalse(belowContentContact)
