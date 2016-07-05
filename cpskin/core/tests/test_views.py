# -*- coding: utf-8 -*-
from cpskin.core.browser.folderview import configure_folderviews
from cpskin.core.interfaces import ICPSkinCoreLayer
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import add_behavior
from cpskin.core.utils import add_leadimage_from_file
from plone import api
from plone.app.testing import TEST_USER_ID, setRoles
from zope.component import getMultiAdapter
from zope.interface import directlyProvides

import unittest


class TestViews(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_opendata_view(self):
        directlyProvides(self.request, ICPSkinCoreLayer)
        configure_folderviews(self.portal)
        self.portal.invokeFactory(
            'collective.directory.directory', 'directory1')
        view = self.portal.restrictedTraverse('opendata')
        links = view.get_links()
        self.assertEqual(len(links), 3)

    def test_folderiew_setting_named_link(self):
        add_behavior(
            'Collection',
            'cpskin.core.behaviors.indexview.ICpskinIndexViewSettings')
        configure_folderviews(self.portal)
        news = api.content.create(
            container=self.portal,
            type='News Item',
            id='testnewsitem')
        api.content.transition(obj=news, transition='publish')
        collection = self.portal.actualites.actualites
        link_text = getattr(collection, 'link_text')
        self.assertEqual(link_text, "Voir l'ensemble des")
        view = getMultiAdapter((self.portal, self.request), name="folderview")
        voir_lensemble_des = view.see_all(collection)
        self.assertEqual(voir_lensemble_des,
                         "Voir l'ensemble des actualit\xc3\xa9s")

        collection.link_text = "Voir toutes les"
        voir_lensemble_des = view.see_all(collection)
        self.assertEqual(voir_lensemble_des,
                         "Voir toutes les actualit\xc3\xa9s")
        # self.assertTrue("Voir toutes les actualit" in view.index())

    def test_folderiew_setting_image_scale(self):
        add_behavior(
            'Collection',
            'cpskin.core.behaviors.indexview.ICpskinIndexViewSettings')
        configure_folderviews(self.portal)
        news = api.content.create(
            container=self.portal,
            type='News Item',
            id='testnewsitem')
        api.content.transition(obj=news, transition='publish')
        collection = self.portal.actualites.actualites
        view = getMultiAdapter(
            (self.portal, self.request), name="folderview")
        self.assertEqual(collection.collection_image_scale, 'mini')
        self.assertEqual(collection.slider_image_scale, 'slider')
        self.assertEqual(collection.carousel_image_scale, 'carousel')
        scale = view.collection_image_scale(collection, news)
        self.assertFalse(scale)
        add_leadimage_from_file(news, 'visuel.png')
        scale = view.collection_image_scale(collection, news)
        self.assertTrue('height="200"' in scale)

        collection.collection_image_scale = 'thumb'
        scale = view.collection_image_scale(collection, news)
        self.assertTrue('height="128"' in scale)

    def test_folderiew_add_remove_content(self):
        configure_folderviews(self.portal)
        request = self.portal.actualites.REQUEST
        news = api.content.create(
            container=self.portal,
            type='News Item',
            id='testnewsitem')
        view = getMultiAdapter(
            (self.portal.actualites, request), name="folderview")
        self.assertTrue(view.canRemoveContent())
        self.assertFalse(view.canAddContent())
        view.removeContent()
        self.assertFalse(view.canRemoveContent())
        self.assertTrue(view.canAddContent())
        view.addContent()
        self.assertTrue(view.canRemoveContent())
        self.assertFalse(view.canAddContent())

    def test_folderiew_render(self):
        configure_folderviews(self.portal)
        request = self.portal.actualites.REQUEST
        news = api.content.create(
            container=self.portal,
            type='News Item',
            id='testnewsitem')
        view = getMultiAdapter(
            (self.portal.actualites, request), name="folderview")
        self.assertIn(
            '<a href="http://nohost/plone/actualites">View</a>', view.index())
