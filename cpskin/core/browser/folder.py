# -*- coding: utf-8 -*-
from cpskin.core.utils import image_scale
from plone import api
from plone.app.contenttypes.browser.folder import FolderView


class CpskinNavigationView(FolderView):

    def menus(self):
        portal_catalog = api.portal.get_tool('portal_catalog')
        context_path = '/'.join(self.context.getPhysicalPath())
        query = {}
        query['review_state'] = 'published_and_shown'
        query['path'] = {'query': context_path, 'depth': 1}
        query['sort_on'] = 'getObjPositionInParent'
        return portal_catalog(query)

    def accesses(self):
        if self.level() < 2:
            return []
        portal_catalog = api.portal.get_tool('portal_catalog')
        context_path = '/'.join(self.context.getPhysicalPath())
        query = {}
        query['path'] = {'query': context_path, 'depth': 10}
        query['sort_on'] = 'sortable_title'
        query['object_provides'] = 'cpskin.menu.interfaces.IDirectAccess'
        return portal_catalog(query)

    def level(self):
        portal = api.portal.get()
        portal_level = len(portal.getPhysicalPath())
        context_level = len(self.context.getPhysicalPath())
        return context_level - portal_level


class CpskinNavigationViewWithLeadImage(FolderView):

    def menus(self):
        portal_catalog = api.portal.get_tool('portal_catalog')
        context_path = '/'.join(self.context.getPhysicalPath())
        query = {}
        query['review_state'] = 'published_and_shown'
        query['path'] = {'query': context_path, 'depth': 1}
        query['sort_on'] = 'getObjPositionInParent'
        return portal_catalog(query)

    def image(self, brain):
        obj = brain.getObject()
        return image_scale(obj, 'leadimage-navigation', 'mini')
