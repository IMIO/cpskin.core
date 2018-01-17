# -*- coding: utf-8 -*-
from Acquisition import aq_base
from collective.contact.core.browser.address import get_address
from collective.geo.behaviour.interfaces import ICoordinates
from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.multilingual.interfaces import IPloneAppMultilingualInstalled
from plone.dexterity.interfaces import IDexterityFTI
from plone.namedfile.file import NamedBlobImage
from Products.CMFCore.interfaces import ISiteRoot
from zope.component import queryUtility

import geocoder
import logging
import os
import phonenumbers
import sys


logger = logging.getLogger('cpskin.core.utils')


def safe_utf8(s):
    """Transform unicode to utf8"""
    if isinstance(s, unicode):
        s = s.encode('utf8')
    return s


def safe_unicode(s):
    """Decode from utf8"""
    if isinstance(s, str):
        s = s.decode('utf8')
    return s


def reactivateTopic():
    """Reactivate old Topic content type"""
    portal = api.portal.get()
    portal.portal_types.Topic.manage_changeProperties(global_allow=True)
    for action in portal.portal_controlpanel.listActions():
        if action.id == 'portal_atct':
            action.visible = True


def convertCollection(collection):
    """Convert a new collection into an old collection"""
    portal = api.portal.get()

    id = collection.id
    title = collection.title
    container = collection.aq_parent
    default_page = container.getDefaultPage()

    api.content.delete(collection)
    allowed_types = container.getLocallyAllowedTypes()
    container.setLocallyAllowedTypes(allowed_types + ('Topic', ))
    old_collection = api.content.create(container=container, type=u'Topic',
                                        id=id, title=title, safe_id=False)
    portal.portal_workflow.doActionFor(old_collection, 'publish')
    container.setLocallyAllowedTypes(allowed_types)
    container.setDefaultPage(default_page)
    return old_collection


def publish_content(content):
    """Publish an object and hide it for cpskin."""
    wftool = api.portal.get_tool('portal_workflow')
    if wftool.getInfoFor(content, 'review_state') != 'published':
        actions = [a.get('id') for a in wftool.listActions(object=content)]
        if api.content.get_state(obj=content) != 'published_and_hidden':
            # we need to handle both workflows
            if 'publish_and_hide' in actions:
                wftool.doActionFor(content, 'publish_and_hide')
            elif 'publish' in actions:
                wftool.doActionFor(content, 'publish')


def set_exclude_from_nav(obj):
    if getattr(obj, 'setExcludeFromNav', None):
        obj.setExcludeFromNav(True)
    else:
        # dexterity with exludefromnav behavior
        obj.exclude_from_nav = True


def add_keyword(obj, tag_id='hiddenTags', tag_value=[]):
    """Add a keyword to a object."""
    old_value = getattr(obj, tag_id)
    if not old_value:
        values = tag_value
    else:
        values = old_value + tag_value
    setattr(obj, tag_id, values)
    obj.reindexObject()


def has_behavior(type_name, behavior_name):
    """Check if a behavior is on portal_type"""
    fti = queryUtility(IDexterityFTI, name=type_name)
    if not fti:
        return
    behaviors = list(fti.behaviors)
    if behavior_name not in behaviors:
        return False
    else:
        return True


def add_behavior(type_name, behavior_name):
    """Add a behavior to a type"""
    fti = queryUtility(IDexterityFTI, name=type_name)
    if not fti:
        return
    behaviors = list(fti.behaviors)
    if behavior_name not in behaviors:
        behaviors.append(behavior_name)
        fti._updateProperty('behaviors', tuple(behaviors))


def remove_behavior(type_name, behavior_name):
    """Add a behavior to a type"""
    fti = queryUtility(IDexterityFTI, name=type_name)
    if not fti:
        return
    behaviors = list(fti.behaviors)
    if behavior_name in behaviors:
        behaviors.remove(behavior_name)
        fti._updateProperty('behaviors', tuple(behaviors))


def add_leadimage_from_file(container, file_name,
                            folder_name='data', image_field='image'):
    """Add leadimage from a file from a folder"""
    if not container:
        container = api.portal.get()
    data_path = os.path.join(os.path.dirname(__file__), folder_name)
    file_path = os.path.join(data_path, file_name)
    if not getattr(aq_base(container), file_name, False):
        namedblobimage = NamedBlobImage(
            data=open(file_path, 'r').read(),
            filename=unicode(file_name)
        )
        image_container = container
        if not INavigationRoot.providedBy(container) and \
                not ISiteRoot.providedBy(container):
            image_container = container.aq_parent

        image = api.content.create(type='Image',
                                   title=file_name,
                                   image=namedblobimage,
                                   container=image_container)
        image.setTitle(file_name)
        image.reindexObject()
        setattr(container, image_field, namedblobimage)


def image_scale(obj, css_class, default_scale, generate_tag=True, with_uid=True):
    images = obj.restrictedTraverse('@@images')
    if obj.portal_type in ['organization', 'person']:
        if getattr(images, 'logo', False):
            image_field_id = 'logo'
            image = images.scale(image_field_id, scale=default_scale)
        else:
            image = None
    else:
        image_field_id = 'image'
        image = images.scale(image_field_id, scale=default_scale)
    if not image:
        return False
    if not generate_tag:
        return image
    if not with_uid:
        image_path = '{0}/@@images/{1}/{2}'.format(
            '/'.join(obj.getPhysicalPath()),
            image_field_id,
            default_scale)
        image.url = image_path
        return image
    return image.tag(css_class=css_class) if image.tag() else ''


# --------------- Address ---------------

def get_lat_lng_from_address(address):
    """Return tuple with status and geocoder object
       0: error, 1: success, 2: not found, 3: unexpected error"""
    try:
        googleapi = 'collective.geo.settings.interfaces.IGeoSettings.googleapi'
        key = api.portal.get_registry_record(googleapi)
        if key:
            geocode = geocoder.google(safe_utf8(address), key=key)
            if geocode.content['status'] == 'REQUEST_DENIED':
                logger.info('Google maps API: {0}'.format(
                    geocode.content['error_message']))
                geocode = geocoder.google(safe_utf8(address))
        else:
            geocode = geocoder.google(safe_utf8(address))
    except:
        try:
            geocode = geocoder.osm(safe_utf8(address))
        except:
            return (3, 'Unexpected error: {0}'.format(sys.exc_info()[0]))
    if geocode.content['status'] == u'OVER_QUERY_LIMIT':
        message = geocode.content['error_message']
        logger.info(message)
        return (0, message)
    if geocode.content['status'] == u'ZERO_RESULTS':
        message = u'No result found for {0}'.format(address.decode('utf8'))
        return (2, message)
    return (1, geocode)


def get_address_from_obj(obj):
    # Event
    loc = getattr(obj, 'location', '')
    if loc:
        return obj.location
    # old card
    if obj.portal_type == 'collective.directory.card':
        street = get_field(obj, 'address')
        zip_code = get_field(obj, 'zip_code')
        city = get_field(obj, 'city')
        address = '{0} {1} {2}'.format(
            street, zip_code, city
        )
        return address

    # collective.contact.core
    dict_address = get_address(obj)
    street = safe_utf8(dict_address.get('street'))
    number = safe_utf8(dict_address.get('number'))
    zip_code = safe_utf8(dict_address.get('zip_code'))
    city = safe_utf8(dict_address.get('city'))
    if street and city:
        address = '{0} {1} {2} {3}'.format(
            number, street, zip_code, city
        )
    else:
        return ''
    return address


def get_field(obj, field_name):
    value = getattr(obj, field_name, '')
    if isinstance(value, int):
        return str(value).encode('utf8')
    if value:
        return value.encode('utf8')
    return ''


def has_lat_lng(obj):
    try:
        if ICoordinates(obj).coordinates:
            return True
    except:  # noqa
        return False
    return False


def set_coord(obj, request):
    if not has_behavior(obj.portal_type, ICoordinates.__identifier__):
        return
    address = get_address_from_obj(obj)
    if address:
        status, geocode = get_lat_lng_from_address(address)
        if status in [0, 2, 3]:
            # 0: stop if limit is 'OVER_QUERY_LIMIT'
            # 2: not found
            # 3: unexpected error
            api.portal.show_message(message=geocode, request=request)
            logger.info(geocode)
        else:
            if geocode.lng and geocode.lat:
                coord = u'POINT({0} {1})'.format(geocode.lng, geocode.lat)
                ICoordinates(obj).coordinates = coord
                obj.reindexObject(
                    idxs=['zgeo_geometry', 'collective_geo_styles'])
                path = '/'.join(obj.getPhysicalPath())
                message = 'lat lng of {0} updated'.format(path)
                logger.info(message)
                return message
    else:
        message = 'No address for <a href="{0}">{1}</a>'.format(
            obj.absolute_url(),
            obj.id
        )
        api.portal.show_message(message=message, request=request)
        logger.info(message)


def format_phone(value):
    try:
        number = phonenumbers.parse(value, 'BE')
    except phonenumbers.NumberParseException:
        return {'raw': value, 'formated': value}
    formated_value = phonenumbers.format_number(
        number,
        phonenumbers.PhoneNumberFormat.INTERNATIONAL,
    )
    country_code = str(number.country_code)
    country_code_with_plus = '+{0}'.format(country_code)
    return {
        'raw': formated_value,
        'formated': formated_value.replace(
            country_code_with_plus,
            '{0} (0)'.format(country_code_with_plus),
        ),
    }


def set_plonecustom_last():
    portal_css = api.portal.get_tool('portal_css')
    resources = list(portal_css.resources)
    custom_id = 'ploneCustom.css'
    if custom_id in [res.getId() for res in resources]:
        portal_css.moveResource(custom_id, len(resources))


def is_plone_app_multilingual_installed(request):
    return IPloneAppMultilingualInstalled.providedBy(request)
