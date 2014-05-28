# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common
from plone import api

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MenuToolsViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('menutools.pt')
    def get_faceted(self):
        view = {}
        page = api.content.get('/naviguer-par-facettes')
        if page:
            view['href'] = page.absolute_url()
            view['title'] = page.title
        return view

    def get_toolbox(self):
        view = {}
        page = api.content.get('/boite-a-outils/boite-a-outils')
        if page:
            view['href'] = page.absolute_url()
            view['title'] = page.title
        return view
