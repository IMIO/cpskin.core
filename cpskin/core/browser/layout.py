# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.globals import layout as base
from plone.app.layout.globals.interfaces import ILayoutPolicy
from zope.interface import implements

from cpskin.citizen.utils import is_citizen


class LayoutPolicy(base.LayoutPolicy):
    """
    Enhanced layout policy
    """
    implements(ILayoutPolicy)

    def bodyClass(self, template, view):
        """
        Extend Plone to add a CSS class on <body> based on :
        1. the 1st level folder of the current context :
         - 'section-theme1' or 'section-theme2' or ... for portal tabs folders
           based on their positions
         - section-notheme if not in a portal tab folder
        2. the citizen user
        3. minisite
        4. homepage
        """
        context = self.context

        # Get default body classes
        body_class = base.LayoutPolicy.bodyClass(self, template, view)

        # Get 1st level folders appearing in navigation
        portal_catalog = api.portal.get_tool(name='portal_catalog')
        navtreeProps = api.portal.get_tool(name='portal_properties').navtree_properties
        navigation_root = api.portal.get_navigation_root(context)
        queryDict = {}
        queryDict['path'] = {'query': '/'.join(navigation_root.getPhysicalPath()), 'depth': 1}
        if navtreeProps.enable_wf_state_filtering:
            queryDict['review_state'] = navtreeProps.wf_states_to_show
        queryDict['sort_on'] = 'getObjPositionInParent'
        queryDict['portal_type'] = 'Folder'
        queryDict['is_default_page'] = False
        brains = portal_catalog(queryDict)
        res = [b for b in brains if b.id not in navtreeProps.idsNotToList]

        # Get the first level of the current
        actual_url_path = '/'.join(context.getPhysicalPath())
        # Check if we are in a theme and check if we are in the right one (position)
        index = 1
        inTheme = False
        for brain in res:
            # checking startswith is not enough
            # see ticket #1227 :
            # if theme1 id is "theme" and theme2 id is "theme2", while being in the
            # theme2, it starts with 'theme' so it returns True to checking if being in theme 1...
            brainPath = brain.getPath()
            if actual_url_path.startswith(brainPath):
                brainPathLen = len(brainPath)
                if len(actual_url_path) == brainPathLen \
                   or actual_url_path[brainPathLen:brainPathLen + 1] == '/':
                    inTheme = True
                    body_class += ' section-theme%s' % index
            index += 1

        if not inTheme:
            body_class += ' section-notheme'

        minisite = self.request.get('cpskin_minisite', None)
        if minisite:
            if minisite.is_in_minisite_mode:
                body_class += ' in-minisite-out-portal'
            if minisite.is_in_portal_mode:
                body_class += ' in-minisite-in-portal'

        if is_main_homepage(context):
            body_class += ' main-homepage'

        user = api.user.get_current()
        if is_citizen(user):
            body_class += ' user-citizen'

        return body_class


def is_main_homepage(context):
    homepage_types = ['LRF', 'Plone Site']
    if context.portal_type in homepage_types:
        return True
    return False
