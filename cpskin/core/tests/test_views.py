# -*- coding: utf-8 -*-
from collective.geo.behaviour.interfaces import ICoordinates
from collective.taxonomy.interfaces import ITaxonomy
from cpskin.core.behaviors.indexview import ICpskinIndexViewSettings
from cpskin.core.browser.folderview import configure_folderviews
from cpskin.core.browser.form import GeoForm
from cpskin.core.interfaces import ICPSkinCoreLayer
from cpskin.core.testing import CPSKIN_CORE_INTEGRATION_TESTING
from cpskin.core.utils import add_behavior
from cpskin.core.utils import add_leadimage_from_file
from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.schemaeditor.utils import FieldAddedEvent
from plone.schemaeditor.utils import IEditableSchema
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form.interfaces import IFormLayer
from zope import schema
from zope.component import getMultiAdapter
from zope.component import queryUtility
from zope.component import provideAdapter
from zope.interface import alsoProvides
from zope.interface import directlyProvides
from zope.interface import Interface
from zope.event import notify
from zope.lifecycleevent import ObjectAddedEvent
from zope.publisher.interfaces.browser import IBrowserRequest
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
        view = getMultiAdapter((self.portal, self.request), name='folderview')
        voir_lensemble_des = view.see_all(collection)
        self.assertEqual(voir_lensemble_des,
                         "Voir l'ensemble des actualit\xc3\xa9s")

        collection.link_text = "Voir toutes les"
        voir_lensemble_des = view.see_all(collection)
        self.assertEqual(voir_lensemble_des,
                         'Voir toutes les actualit\xc3\xa9s')
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
        api.content.create(
            container=self.portal,
            type='News Item',
            id='testnewsitem')
        view = getMultiAdapter(
            (self.portal.actualites, request), name='folderview')
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
        api.content.create(
            container=self.portal,
            type='News Item',
            id='testnewsitem')
        view = getMultiAdapter(
            (self.portal.actualites, request), name='folderview')
        self.assertIn(
            '<a href="http://nohost/plone/actualites">View</a>', view.index())

    def test_folderiew_event_category(self):
        applyProfile(self.portal, 'collective.taxonomy:default')
        add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)

        utility = queryUtility(ITaxonomy, name='collective.taxonomy.test')
        collection = api.content.create(container=self.portal,
                                        type='Collection',
                                        id='collection')
        collection.taxonomy_category = 'taxonomy_test'
        collection.reindexObject()

        taxonomy_test = schema.Set(
            title=u"taxonomy_test",
            description=u"taxonomy description schema",
            required=False,
            value_type=schema.Choice(
                vocabulary=u"collective.taxonomy.taxonomies"),
        )
        portal_types = api.portal.get_tool('portal_types')
        fti = portal_types.get('Event')
        event_schema = fti.lookupSchema()
        schemaeditor = IEditableSchema(event_schema)
        schemaeditor.addField(taxonomy_test, name='taxonomy_test')
        notify(ObjectAddedEvent(taxonomy_test, event_schema))
        notify(FieldAddedEvent(fti, taxonomy_test))
        event = api.content.create(
            container=self.portal,
            type='Event',
            id='testevent')
        simple_tax = [val for val in utility.data['en'].values()]
        event.taxonomy_test = set(simple_tax[0])

        view = getMultiAdapter(
            (self.portal, self.portal.REQUEST), name='folderview')

        see_categories = view.see_categories(collection)
        self.assertTrue(see_categories)
        collection.taxonomy_category = ''
        see_categories = view.see_categories(collection)
        self.assertFalse(see_categories)
        collection.taxonomy_category = 'taxonomy_test'

        # categories = view.get_categories(collection, event)
        # self.assertEqual(categories, ['Information Science'])

    def test_folderiew_event_localizedtime(self):
        event = api.content.create(
            container=self.portal,
            type='Event',
            id='testevent')
        from datetime import datetime
        import pytz
        now = datetime.now(pytz.utc)
        tomorrow = datetime(now.year, now.month, now.day + 1)
        tomorrow.replace(tzinfo=pytz.utc)
        event.start = now
        event.end = now
        view = getMultiAdapter(
            (self.portal, self.portal.REQUEST), name='folderview')

        oneday = view.is_one_day(event)
        self.assertTrue(oneday)

        event.end = tomorrow
        oneday = view.is_one_day(event)
        self.assertFalse(oneday)

        withhours = view.is_with_hours(event)
        self.assertTrue(withhours)

    def test_event_geo_contents_view(self):
        add_behavior('Event', ICoordinates.__identifier__)
        event = api.content.create(container=self.portal,
                           type='Event', title='document')
        event.location = 'Zoning Industriel, 34 5190 Mornimont'
        form = getMultiAdapter(
            (self.portal, self.portal.REQUEST), name='set-geo-contents-form')
        form.request.form = {'form.widgets.content_types': [u'Event']}
        form.update()
        data, errors = form.extractData()
        self.assertEqual(len(errors), 0)
        coord = ICoordinates(event).coordinates
        self.assertFalse(coord.startswith('POINT '))
        form.handleApply(form, 'Ok')
        coord = ICoordinates(event).coordinates
        self.assertTrue(coord.startswith('POINT '))

    def test_orga_geo_contents_view(self):
        # add some contacts
        applyProfile(self.portal, 'collective.contact.core:default')
        directory = api.content.create(
            container=self.portal, type='directory', id='directory')
        person = api.content.create(
            container=directory, type='person', id='person')
        person.street = u'Zoning Industriel'
        person.number = u'34'
        person.zip_code = u'5190'
        person.city = u'Mornimont'

        add_behavior('person', ICoordinates.__identifier__)

        form = getMultiAdapter(
            (self.portal, self.portal.REQUEST), name='set-geo-contents-form')
        form.request.form = {'form.widgets.content_types': [u'person']}
        form.update()

        coord = ICoordinates(person).coordinates
        self.assertFalse(coord.startswith('POINT '))
        form.handleApply(form, 'Ok')
        coord = ICoordinates(person).coordinates
        self.assertTrue(coord.startswith('POINT '))

    def test_bad_orga_geo_contents_view(self):
        # add some contacts
        applyProfile(self.portal, 'collective.contact.core:default')
        add_behavior('person', ICoordinates.__identifier__)
        directory = api.content.create(
            container=self.portal, type='directory', id='directory')
        person = api.content.create(
            container=directory, type='person', id='person')

        form = getMultiAdapter(
            (self.portal, self.portal.REQUEST), name='set-geo-contents-form')
        form.request.form = {'form.widgets.content_types': [u'person']}
        form.update()
        form.handleApply(form, 'Ok')
        messages = IStatusMessage(self.portal.REQUEST).showStatusMessages()
        self.assertEqual(messages[0].message, u'No address for /plone/directory/person')
        self.assertEqual(messages[1].message, u'0 person are updated')
        person.street = u'Zoning Industriél'
        person.number = u'34'
        person.zip_code = u'5190'
        person.city = u'Mornimônt'

        form = getMultiAdapter(
            (self.portal, self.portal.REQUEST), name='set-geo-contents-form')
        form.request.form = {'form.widgets.content_types': [u'person']}
        form.update()

        coord = ICoordinates(person).coordinates
        self.assertFalse(coord.startswith('POINT '))
        form.handleApply(form, 'Ok')
        messages = IStatusMessage(self.portal.REQUEST).showStatusMessages()
        self.assertEqual(messages[0].message, u'1 person are updated')
        coord = ICoordinates(person).coordinates
        self.assertTrue(coord.startswith('POINT '))
