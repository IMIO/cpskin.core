# -*- coding: utf-8 -*-
from cpskin.core.behaviors.metadata import IHiddenTags
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import add_behavior
from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
import unittest


class TestVocabularies(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_contact_fields_vocabulary(self):
        applyProfile(self.portal, 'collective.contact.core:default')
        name = 'cpskin.core.vocabularies.contact_fields'
        factory = getUtility(IVocabularyFactory, name)
        vocabulary = factory(self.portal)
        keys = vocabulary.by_value.keys()
        self.assertNotIn('im_handle', keys)
        self.assertIn('street', keys)
        self.assertIn('number', keys)
        self.assertIn('zip_code', keys)
        self.assertIn('city', keys)
        self.assertIn('activity', keys)
        self.assertIn('title', keys)
        titles = [val.title for val in vocabulary.by_value.values()]
        self.assertIn(u'Contact details: Email', titles)

    def test_hidden_tags_vocabulary(self):
        name = 'cpskin.core.vocabularies.hiddenTags'
        factory = getUtility(IVocabularyFactory, name)
        vocabulary = factory(self.portal)
        keys = vocabulary.by_value.keys()
        self.assertEqual(keys, [u'a-la-une', u'homepage'])
        add_behavior('Document', IHiddenTags.__identifier__)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(container=self.portal,
                           type='Document', title='document')
        document = self.portal.document
        document.hiddenTags = [u'mot clé caché']
        document.reindexObject()
        vocabulary = factory(self.portal)
        keys = vocabulary.by_value.keys()
        self.assertEqual(
            keys, [u'mot cl\xe9 cach\xe9', u'a-la-une', u'homepage'])
