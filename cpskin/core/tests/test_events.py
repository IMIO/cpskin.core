
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
from zope.lifecycleevent import ObjectModifiedEvent
from zope.publisher.interfaces.browser import IBrowserRequest
import unittest


class TestEvents(unittest.TestCase):

    layer = CPSKIN_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_modified_orga_events(self):
        # add some contacts
        applyProfile(self.portal, 'collective.contact.core:default')
        add_behavior('organization', ICoordinates.__identifier__)
        directory = api.content.create(
            container=self.portal, type='directory', id='directory')
        orga = api.content.create(
            container=directory, type='organization', id='orga')
        orga.street = u'Zoning Industriel'
        orga.number = u'34'
        # notify(ObjectAddedEvent(orga))
        coord = ICoordinates(orga).coordinates
        self.assertFalse(coord.startswith('POINT '))
        orga.zip_code = u'5190'
        orga.city = u'Mornimont'
        notify(ObjectModifiedEvent(orga))
        coord = ICoordinates(orga).coordinates
        self.assertTrue(coord.startswith('POINT '))
