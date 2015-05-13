# -*- coding: utf-8 -*-
from zope.interface import directlyProvides, directlyProvidedBy
from Products.CMFCore.utils import getToolByName

from plone import api

from cpskin.core.setuphandlers import setPageText, addLoadPageMenuToRegistry
from cpskin.core.setuphandlers import addAutoPlaySliderToRegistry
from cpskin.core.setuphandlers import addSliderTimerToRegistry

import logging
logger = logging.getLogger('cpskin.core')


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
                             roles=['Portlets Manager', 'Manager', 'Site Administrator'],
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
            cleanedProvided = [i for i in provided if i.__identifier__ != interface]
            directlyProvides(obj, cleanedProvided)
            obj.reindexObject()

    portal_javascripts = api.portal.get_tool('portal_javascripts')
    portal_javascripts.unregisterResource('++resource++cpskin.core.menutools.js')


def upgrade_to_four(context):
    addLoadPageMenuToRegistry()


def upgrade_to_three(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'actions')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'rolemap')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'sharing')
    portal = api.portal.get()
    portal.manage_permission('Portlets: Manage portlets',
                             roles=['Editor', 'Portlets Manager', 'Manager', 'Site Administrator'],
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
