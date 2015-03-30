# -*- coding: utf-8 -*-
from Acquisition import aq_inner

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import ViewletBase

from Products.CMFCore.utils import getToolByName

from plone import api


class CPSkinFooterSitemapViewlet(ViewletBase):
    render = ViewPageTemplateFile('footersitemap.pt')

    def createSiteMap(self):
        context = aq_inner(self.context)
        # take the 2 first levels of the site that respect the navigation strategy
        portal_catalog = getToolByName(context, 'portal_catalog')
        navtreeProps = getToolByName(context, 'portal_properties').navtree_properties
        portal = getToolByName(context, 'portal_url').getPortalObject()
        queryDict = {}
        navigation_root = api.portal.get_navigation_root(context)
        queryDict['path'] = {'query': '/'.join(navigation_root.getPhysicalPath()), 'depth': 1}
        if navtreeProps.enable_wf_state_filtering:
            queryDict['review_state'] = navtreeProps.wf_states_to_show
        queryDict['sort_on'] = 'getObjPositionInParent'
        themes = portal_catalog(queryDict)
        res = []
        metaTypesNotToList = navtreeProps.metaTypesNotToList
        idsNotToList = navtreeProps.idsNotToList
        for theme in themes:
            if not theme.meta_type in metaTypesNotToList and \
               not theme.id in idsNotToList and not theme.exclude_from_nav:
                themeRes = {'theme': theme, 'children': []}
                # do a second catalog_search by theme
                queryDict['path'] = {'query': theme.getPath(), 'depth': 1}
                children = portal_catalog(queryDict)
                for child in children:
                    if not child.meta_type in metaTypesNotToList and \
                       not child.id in idsNotToList and not child.exclude_from_nav:
                        themeRes['children'].append(child)
                res.append(themeRes)
        return res

    def getFooterText(self):
        footer_static = getattr(self.context, 'footer-static', None)
        if footer_static is None:
            return
        if footer_static.Language() == self.context.Language():
            return footer_static.getText()
        if hasattr(footer_static, 'getTranslation'):
            lang = self.context.REQUEST.get('LANGUAGE', 'fr')
            footer_static = footer_static.getTranslation(lang)
        return footer_static.getText()
