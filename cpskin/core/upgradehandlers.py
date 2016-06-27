# -*- coding: utf-8 -*-
from cpskin.core.behaviors.indexview import ICpskinIndexViewSettings
from cpskin.core.setuphandlers import add_homepage_keywords
from cpskin.core.setuphandlers import addAutoPlaySliderToRegistry
from cpskin.core.setuphandlers import addCityNameToRegistry
from cpskin.core.setuphandlers import addLoadPageMenuToRegistry
from cpskin.core.setuphandlers import addSliderTimerToRegistry
from cpskin.core.setuphandlers import addSliderTypeToRegistry
from cpskin.core.setuphandlers import addSubMenuPersistenceToRegistry
from cpskin.core.setuphandlers import setPageText
from cpskin.core.utils import add_behavior
from plone import api
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from zope.interface import directlyProvides, directlyProvidedBy

import logging
logger = logging.getLogger('cpskin.core')


def add_index_view_behavior(context):
    registry = getUtility(IRegistry)
    del registry.records[
        'cpskin.core.interfaces.ICPSkinSettings.homepage_keywords']
    add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)


def upgrade_homepage_keywords(context):
    add_homepage_keywords()


def upgrade_minisite_menu(context):
    # add new viewlet cpskin.minisite
    context.runImportStepFromProfile('profile-cpskin.core:default', 'viewlets')
    context.runImportStepFromProfile(
        'profile-cpskin.menu:default', 'jsregistry')
    context.runImportStepFromProfile(
        'profile-cpskin.minisite:default', 'actions')


def upgrade_city_name(context):
    addCityNameToRegistry()


def upgrade_slider_type(context):
    addSliderTypeToRegistry()


def upgrade_footer_viewlet(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'viewlets')


def upgrade_to_eleven(context):
    addSubMenuPersistenceToRegistry()


def upgrade_to_eight(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'rolemap')


def upgrade_to_seven(context):
    addAutoPlaySliderToRegistry()
    addSliderTimerToRegistry()


def upgrade_to_six(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'rolemap')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'sharing')
    portal = api.portal.get()
    portal.manage_permission('CPSkin: Edit keywords',
                             roles=['Portlets Manager',
                                    'Manager', 'Site Administrator'],
                             acquire=True)
    site_properties = api.portal.get_tool('portal_properties').site_properties
    site_properties.allowRolesToAddKeywords = ("Manager",
                                               "Site Administrator",
                                               "Portlets Manager")


def upgrade_to_five(context):
    interfaces = ['cpskin.core.viewlets.interfaces.IViewletMenuToolsBox',
                  'cpskin.core.viewlets.interfaces.IViewletMenuToolsFaceted']
    catalog = api.portal.get_tool('portal_catalog')
    for interface in interfaces:
        brains = catalog({"object_provides": interface})
        for brain in brains:
            obj = brain.getObject()
            provided = directlyProvidedBy(obj)
            cleanedProvided = [
                i for i in provided if i.__identifier__ != interface]
            directlyProvides(obj, cleanedProvided)
            obj.reindexObject()

    portal_javascripts = api.portal.get_tool('portal_javascripts')
    portal_javascripts.unregisterResource(
        '++resource++cpskin.core.menutools.js')


def upgrade_to_four(context):
    addLoadPageMenuToRegistry()


def upgrade_to_three(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'actions')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'rolemap')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'sharing')
    portal = api.portal.get()
    portal.manage_permission('Portlets: Manage portlets',
                             roles=['Editor', 'Portlets Manager',
                                    'Manager', 'Site Administrator'],
                             acquire=True)


def upgrade_to_two(context):
    context.runAllImportStepsFromProfile('profile-cpskin.policy:default')
    portal_catalog = getToolByName(context, 'portal_catalog')
    portal_atct = getToolByName(context, 'portal_atct')
    attrs = ('IAmTags', 'HiddenTags', 'ISearchTags')
    for attr in attrs:
        if attr in portal_catalog.indexes():
            portal_catalog.delIndex(attr)
        if attr in portal_atct.topic_indexes:
            portal_atct.removeIndex(attr)
    for brain in portal_catalog.searchResults():
        obj = brain.getObject()
        for attr in attrs:
            if hasattr(obj, attr):
                try:
                    delattr(obj, attr)
                except AttributeError:
                    logger.info("No {} on: {}".format(attr, obj))


def upgrade_front_page(context):
    portal = api.portal.get()
    if not portal.hasObject('front-page'):
        frontPage = api.content.create(
            container=portal,
            type='Document',
            id='front-page',
            title='Bienvenue chez IMIO'
        )
    else:
        frontPage = getattr(portal, 'front-page', None)
    if frontPage is not None:
        frontPage.setExcludeFromNav(True)
    setPageText(portal, frontPage, 'cpskin-frontpage-setup')
