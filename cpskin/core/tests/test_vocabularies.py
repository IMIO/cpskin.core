# -*- coding: utf-8 -*-
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from plone.app.testing import applyProfile
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest


class TestVocabularies(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_contact_fields_vocabulary(self):
        applyProfile(self.portal, 'collective.contact.core:default')
        name = 'cpskin.core.vocabularies.contactFields'
        factory = getUtility(IVocabularyFactory, name)
        vocabulary = factory(self.portal)
        keys = vocabulary.by_value.keys()
        self.assertNotIn('im_handle', keys)
        self.assertIn('street', keys)
        self.assertIn('number', keys)
        self.assertIn('zip_code', keys)
        self.assertIn('city', keys)
        self.assertIn('title', keys)
