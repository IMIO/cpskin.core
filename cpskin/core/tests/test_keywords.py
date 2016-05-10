# -*- coding: utf-8 -*-
from cpskin.core.browser.folderview import configure_folderviews
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import add_behavior
from cpskin.core.utils import add_keyword
from plone import api
from plone.app.testing import TEST_USER_ID, setRoles
from zope.component import getMultiAdapter

import unittest


class TestKeywords(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        configure_folderviews(self.portal)

    def test_keyword_homepage_behavior(self):
        add_behavior(
            'Collection',
            'cpskin.core.behaviors.metadata.IUseKeywordHomepage')
        collection = api.content.create(
            container=self.portal,
            type='Collection',
            id='testcollection')
        self.assertFalse(getattr(collection, 'useKeywordHomepage'))
        collection.useKeywordHomepage = True
        self.assertTrue(getattr(collection, 'useKeywordHomepage'))

    def test_folderview_without_keyword_homepage(self):
        add_behavior(
            'Collection',
            'cpskin.core.behaviors.metadata.IUseKeywordHomepage')
        add_behavior('News Item', 'cpskin.core.behaviors.metadata.IHiddenTags')
        self.assertFalse(self.portal.actualites.actualites.useKeywordHomepage)
        view = getMultiAdapter((self.portal, self.request), name="folderview")
        result = view.getResults(self.portal.actualites.actualites)
        self.assertTrue(result is None)

        # Adding content for fill collection
        news = api.content.create(
            container=self.portal,
            type='News Item',
            id='testnewsitem')
        api.content.transition(obj=news, transition='publish')
        result = view.getResults(self.portal.actualites.actualites)
        self.assertEqual(len(result.get('standard-results', 0)), 1)

        add_keyword(news, 'hiddenTags', ['homepage'])
        add_keyword(news, 'hiddenTags', ['non-homepage'])

        result = view.getResults(self.portal.actualites.actualites)
        self.assertEqual(len(result.get('standard-results', 0)), 1)

    def test_folderview_with_keyword_homepage(self):
        add_behavior(
            'Collection',
            'cpskin.core.behaviors.metadata.IUseKeywordHomepage')
        add_behavior('News Item', 'cpskin.core.behaviors.metadata.IHiddenTags')
        self.portal.actualites.actualites.useKeywordHomepage = True
        self.assertTrue(self.portal.actualites.actualites.useKeywordHomepage)
        view = getMultiAdapter((self.portal, self.request), name="folderview")
        news = api.content.create(
            container=self.portal,
            type='News Item',
            id='testnewsitem')
        api.content.transition(obj=news, transition='publish')
        result = view.getResults(self.portal.actualites.actualites)
        self.assertTrue(result is None)

        add_keyword(news, 'hiddenTags', ['non-homepage'])
        result = view.getResults(self.portal.actualites.actualites)
        self.assertTrue(result is None)

        add_keyword(news, 'hiddenTags', ['homepage'])
        result = view.getResults(self.portal.actualites.actualites)
        self.assertEqual(len(result.get('standard-results', 0)), 1)
