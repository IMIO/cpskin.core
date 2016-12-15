# -*- coding: utf-8 -*-
from cpskin.core.behaviors.indexview import ICpskinIndexViewSettings
from cpskin.core.behaviors.metadata import IHiddenTags
from cpskin.core.behaviors.metadata import IRelatedContacts
from cpskin.core.interfaces import ICPSkinCoreLayer
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import add_behavior
from cpskin.core.utils import remove_behavior
from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.interface import alsoProvides

import unittest


class TestBehaviors(unittest.TestCase):

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
        self.portal.invokeFactory('Collection', 'collection')
        self.collection = self.portal.collection

    def test_use_slider_image_scale(self):
        add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)
        slider_image_scale = getattr(self.collection, 'slider_image_scale')
        self.assertEqual(slider_image_scale, 'slider')
        remove_behavior('Collection', ICpskinIndexViewSettings.__identifier__)

    def test_use_carousel_image_scale(self):
        add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)
        carousel_image_scale = getattr(self.collection, 'carousel_image_scale')
        self.assertEqual(carousel_image_scale, 'carousel')

    def test_use_link_text(self):
        add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)
        link_text = getattr(self.collection, 'link_text')
        self.assertEqual(link_text, "Voir l'ensemble des")

    def test_use_keyword_homepage(self):
        add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)
        index_view_keywords = getattr(self.collection, 'index_view_keywords')
        self.assertEqual(index_view_keywords, None,
                         'Index view keyword is empty by default')

    def test_related_contacts(self):
        add_behavior('Document', IRelatedContacts.__identifier__)
        aboveContentContact = getattr(self.document, 'aboveContentContact')
        self.assertEqual(aboveContentContact, [])
        belowContentContact = getattr(self.document, 'belowContentContact')
        self.assertFalse(belowContentContact)
        remove_behavior('Document', IRelatedContacts.__identifier__)

    def test_hidden_tags(self):
        add_behavior('Document', IHiddenTags.__identifier__)
        hiddenTags = getattr(self.document, 'hiddenTags')
        self.assertEqual(hiddenTags, None)
        self.document.hiddenTags = ('mon-test',)
        self.document.reindexObject()
        hiddenTags = getattr(self.document, 'hiddenTags')
        self.assertEqual(hiddenTags, ('mon-test',))
        catalog = api.portal.get_tool('portal_catalog')
        query = {'hiddenTags': 'mon-test'}
        brains = catalog(query)
        self.assertEqual(len(brains), 1)
        self.assertEqual(brains[0].getObject(), self.document)

    def test_taxonomy_category(self):
        applyProfile(self.portal, 'collective.taxonomy:default')
        add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)
        test_taxonomy_category = getattr(self.collection, 'taxonomy_category')
        self.assertEqual(test_taxonomy_category, '')

    def test_indexview_hide_title(self):
        add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)
        hide_title = getattr(self.collection, 'hide_title')
        self.assertEqual(hide_title, False)
