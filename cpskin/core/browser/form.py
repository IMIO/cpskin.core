# -*- coding: utf-8 -*-
from collective.geo.behaviour.interfaces import ICoordinates
from cpskin.locales import CPSkinMessageFactory as _
from plone import api
from plone.directives import form
from Products.CMFCore.interfaces import ISiteRoot
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button
from zope import schema


import logging
import geocoder

logger = logging.getLogger('cpskin.core.encode_lat_lng')


class IGeoForm(form.Schema):
    """ Define form fields """

    content_types = schema.List(
        title=_(u'Content type'),
        description=_(
            u'Which content type should be set latitude and longitude'),
        value_type=schema.Choice(
            title=_(u'Content types'),
            vocabulary='cpskin.core.vocabularies.geo_types',
        ),
        required=False,
    )


class GeoForm(form.SchemaForm):

    schema = IGeoForm
    ignoreContext = True

    label = u"What's object do you want to update ?"
    description = u"This script will update latitude and longitude for objects \
                    selected"

    @button.buttonAndHandler(u'Ok')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        # Do something with valid data here

        # Set status on this form page
        # (this status message is not bind to the session and does not go thru redirects)
        results = []
        if 'content_types' not in data.keys():
            pass
        else:
            for portal_type in data['content_types']:
                list_updated = set_lat_lng(portal_type, self.request)
                results.extend(list_updated)
                message = '{1} {0} are updated'.format(
                    portal_type, len(list_updated))
                api.portal.show_message(message=message, request=self.request)
        # self.status = "\n".join(results)

    @button.buttonAndHandler(u"Cancel")
    def handleCancel(self, action):
        """User cancelled. Redirect back to the front page.
        """


def has_lat_lng(obj):
    if ICoordinates(obj).coordinates:
        return True
    return False


def set_lat_lng(portal_type, request):
    catalog = api.portal.get_tool('portal_catalog')
    query = {}
    query['portal_type'] = portal_type
    brains = catalog(query)
    nbre = len(brains)
    results = []
    i = 0
    for brain in brains:
        obj = brain.getObject()
        i += 1
        if not has_lat_lng(obj):
            address = get_address_from_obj(obj)
            if address:
                geocode = get_lat_lng_from_address(address, request)
                if not geocode:
                    # stop if limit is 'OVER_QUERY_LIMIT'
                    return results
                if geocode.lng and geocode.lat:
                    coord = u"POINT({0} {1})".format(geocode.lng, geocode.lat)
                    ICoordinates(obj).coordinates = coord
                    path = '/'.join(obj.getPhysicalPath())
                    message = 'lat lng of {0} updated ({1}/{2})'.format(
                        path, i, nbre)
                    logger.info(message)
                    obj.reindexObject()
                    results.append(message)
            else:
                message = 'No address for {0}'.format('/'.join(
                    obj.getPhysicalPath()))
                api.portal.show_message(message=message, request=request)
                logger.warn(message)
    return results


def get_address_from_obj(obj):
    # Event
    loc = getattr(obj, 'location', '')
    if loc:
        return obj.location

    # collective.contact.core
    street = get_field(obj, 'street')
    number = get_field(obj, 'number')
    zip_code = get_field(obj, 'zip_code')
    city = get_field(obj, 'city')
    if street and city:
        address = '{} {} {} {}'.format(
            number, street, zip_code, city
        )
    else:
        return ''
    return address


def get_lat_lng_from_address(address, request):
    geocode = geocoder.google(address)
    if geocode.content['status'] == u'OVER_QUERY_LIMIT':
        logger.info(geocode.content['error_message'])
        return False
    if geocode.content['status'] == u'ZERO_RESULTS':
        message = u'No result found for {0}'.format(address.decode('utf8'))
        api.portal.show_message(message=message, request=request)
        return geocode
    return geocode

def get_field(obj, field_name):
    value = getattr(obj, field_name, '')
    if value:
        return value.encode('utf8')
    return ''
