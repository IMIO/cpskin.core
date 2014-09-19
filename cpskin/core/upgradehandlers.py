# -*- coding: utf-8 -*-
from zope.component import queryUtility
from Products.CMFCore.utils import getToolByName

from plone import api
from plone.registry.interfaces import IRegistry
from plone.registry import field, Record

from cpskin.core.setuphandlers import setPageText
from cpskin.locales import CPSkinMessageFactory as _

import logging
logger = logging.getLogger('cpskin.core')


def upgrade_to_four(context):
    logger.info("Adding cpskin.core.interfaces.ICPSkinSettings.load_page_menu to registry")
    registry = queryUtility(IRegistry)

    record = Record(field.Bool(title=_(u"Load page menu"),
                               description=_(u"Is level 1 menu load page at click?"),
                               required=False,
                               default=False),
                    value=False)

    registry.records['cpskin.core.interfaces.ICPSkinSettings.load_page_menu'] = record


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
