# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName


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
                delattr(obj, attr)
