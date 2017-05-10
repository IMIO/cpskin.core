# -*- coding: utf-8 -*-

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.layout.viewlets import common

from cpskin.core.interfaces import IElectedContentForTopMenu


class TopMenuViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('top_menu.pt')

    def menus(self):
        portal_catalog = api.portal.get_tool('portal_catalog')
        interface_name = IElectedContentForTopMenu.__identifier__
        query = {'object_provides': interface_name}
        results = portal_catalog.searchResults(query)
        results = [r for r in results if r.exclude_from_nav]
        menus = []
        for r in results:
            query_path = {'query': r.getPath(), 'depth': 1}
            sub_items = api.content.find(path=query_path)
            sub_items = [s for s in sub_items if not s.exclude_from_nav]
            menu_item = {
                'root': r,
                'submenu': sub_items,
            }
            menus.append(menu_item)
        return menus
