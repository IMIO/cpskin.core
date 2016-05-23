# -*- coding: utf-8 -*-
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import add_behavior
from cpskin.core.utils import add_keyword
from cpskin.core.utils import add_leadimage_from_file
from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import TEST_USER_ID, setRoles
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryMultiAdapter
from zope.intid.interfaces import IIntIds
from zope.viewlet.interfaces import IViewletManager
from z3c.relationfield.relation import RelationValue
import unittest


class TestViewlets(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_set_media_viewlet(self):
        view = getMultiAdapter(
            (self.portal, self.request), name="media_activation")
        self.assertFalse('videos' in self.portal.keys())
        self.assertFalse(view.is_enabled)
        self.assertFalse(view.can_disable_media)

        view.enable_media()
        self.assertTrue(view.is_enabled)
        self.assertTrue(view.can_disable_media)
        self.assertTrue('videos' in self.portal.keys())

        view.disable_media()
        self.assertFalse(view.is_enabled)
        self.assertFalse(view.can_disable_media)
        self.assertTrue('videos' in self.portal.keys())

        view.enable_media()
        self.assertTrue(view.is_enabled)
        self.assertTrue(view.can_disable_media)
        self.assertTrue('videos' in self.portal.keys())

    def test_media_viewlet(self):
        keywords = ['album-a-la-une']
        view = getMultiAdapter(
            (self.portal, self.request), name="media_activation")
        # create video collection used to viewlet
        view.enable_media()
        album_collection = self.portal.albums.index
        query = [
            {
                'i': 'hiddenTags',
                'o': 'plone.app.querystring.operation.selection.is',
                'v': keywords
            },
        ]

        # Set hiddenTags and leadimage behaviors
        add_behavior('Folder', 'cpskin.core.behaviors.metadata.IHiddenTags')
        add_behavior(
            'Folder',
            'plone.app.contenttypes.behaviors.leadimage.ILeadImage')

        album_collection.query = query
        album = api.content.create(
            container=self.portal, type="Folder", id="testalbum")

        # getting viewlet
        view = BrowserView(self.portal, self.request)
        manager_name = 'plone.belowcontent'
        manager = queryMultiAdapter(
            (self.portal, self.request, view),
            IViewletManager,
            manager_name,
            default=None)
        self.assertIsNotNone(manager)
        manager.update()

        my_viewlet = [
            v for v in manager.viewlets if v.__name__ == 'cpskin.media']
        self.assertEqual(len(my_viewlet), 1)
        media_viewlet = my_viewlet[0]

        self.assertTrue(media_viewlet.available())
        self.assertEqual(
            media_viewlet.get_albums_collection().getPhysicalPath(),
            self.portal.albums.index.getPhysicalPath())
        self.assertEqual(len(media_viewlet.get_albums()), 0)

        # Set lead image to album folder
        add_leadimage_from_file(album, "cpskinlogo.png")
        add_keyword(album, 'hiddenTags', keywords)

        self.assertEqual(len(media_viewlet.get_albums()), 1)

    def test_above_related_contacts_viewlet(self):
        add_behavior(
            'Event', 'cpskin.core.behaviors.metadata.IRelatedContacts')
        event = api.content.create(
            container=self.portal,
            type="Event",
            id="myevent"
        )

        # getting viewlet
        view = BrowserView(event, self.request)
        manager_name = 'plone.abovecontentbody'
        manager = queryMultiAdapter(
            (event, self.request, view),
            IViewletManager,
            manager_name,
            default=None)
        self.assertIsNotNone(manager)
        manager.update()

        my_viewlet = [
            v for v in manager.viewlets if v.__name__ == 'cpskin.above_related_contacts']
        self.assertEqual(len(my_viewlet), 1)
        above_viewlet = my_viewlet[0]

        contacts = above_viewlet.get_contacts()
        self.assertEqual(contacts, [])
        self.assertFalse(above_viewlet.available())

        # add some contacts
        applyProfile(self.portal, 'collective.contact.core:default')
        directory = api.content.create(
            container=self.portal, type='directory', id='directory')
        person = api.content.create(
            container=directory, type='person', id='person')
        person.firstname = u'Foo'
        person.lastname = u'Bar'
        person.gender = u'F'
        person.street = u'Zoning Industriel'
        person.number = u'34'
        person.zip_code = u'5190'
        person.city = u'Mornimont'

        # set related contact
        intids = getUtility(IIntIds)
        to_id = intids.getId(person)
        rv = RelationValue(to_id)
        event.aboveContentContact = event.aboveContentContact + [rv]
        self.assertTrue(above_viewlet.available())
        contacts = above_viewlet.get_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0], person)

        self.assertIn('Mornimont', above_viewlet.render())
        self.assertNotIn('Foo Bar', above_viewlet.render())

        event.aboveSeeTitle = True
        self.assertIn('Mornimont', above_viewlet.render())
        self.assertIn('Foo Bar', above_viewlet.render())

    def test_below_related_contacts_viewlet(self):
        add_behavior(
            'Event', 'cpskin.core.behaviors.metadata.IRelatedContacts')
        event = api.content.create(
            container=self.portal,
            type="Event",
            id="myevent"
        )

        # getting viewlet
        view = BrowserView(event, self.request)
        manager_name = 'plone.belowcontentbody'
        manager = queryMultiAdapter(
            (event, self.request, view),
            IViewletManager,
            manager_name,
            default=None)
        self.assertIsNotNone(manager)
        manager.update()

        my_viewlet = [
            v for v in manager.viewlets if v.__name__ == 'cpskin.below_related_contacts']
        self.assertEqual(len(my_viewlet), 1)
        below_viewlet = my_viewlet[0]

        contacts = below_viewlet.get_contacts()
        self.assertEqual(contacts, [])
        self.assertFalse(below_viewlet.available())

        # add some contacts
        applyProfile(self.portal, 'collective.contact.core:default')
        directory = api.content.create(
            container=self.portal, type='directory', id='directory')
        person = api.content.create(
            container=directory, type='person', id='person')
        person.firstname = u'Foo'
        person.lastname = u'Bar'
        person.gender = u'F'
        person.street = u'Zoning Industriel'
        person.number = u'34'
        person.zip_code = u'5190'
        person.city = u'Mornimont'

        # set related contact
        intids = getUtility(IIntIds)
        to_id = intids.getId(person)
        rv = RelationValue(to_id)
        event.belowContentContact = event.belowContentContact + [rv]
        self.assertTrue(below_viewlet.available())
        contacts = below_viewlet.get_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0], person)

        self.assertNotIn('Mornimont', below_viewlet.render())
        self.assertIn('Foo Bar', below_viewlet.render())

        event.belowSeeCoord = True
        self.assertIn('Mornimont', below_viewlet.render())
        self.assertIn('Foo Bar', below_viewlet.render())
