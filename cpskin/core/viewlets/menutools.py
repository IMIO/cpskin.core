# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common
from plone import api

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MenuToolsViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('menutools.pt')
    def get_faceted(self):
        view = {}
        view['href'] = 'naviguer-par-facettes'
        view['title'] = u'Naviguer par facettes'
        return view

    def get_toolbox(self):
        view = {}
        view['href'] = 'boite-a-outils'
        view['title'] = u'Boite à outils'
        return view

    def get_overlay(self):
        page = api.content.get('/boite-a-outils/boite-a-outils')
        return page.getText()
