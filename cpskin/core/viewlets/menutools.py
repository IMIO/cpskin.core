# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common
from plone import api

from cpskin.core.viewlets.interfaces import IViewletMenuToolsFaceted
from cpskin.core.viewlets.interfaces import IViewletMenuToolsBox

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MenuToolsViewlet(common.ViewletBase):

    index = ViewPageTemplateFile('menutools.pt')

    @property
    def portal_catalog(self):
        return api.portal.get_tool(name='portal_catalog')

    def get_faceted(self):
        menutools = []
        brains = self.portal_catalog(
            object_provides=IViewletMenuToolsFaceted.__identifier__,
            sort_on='getObjPositionInParent',
            review_state='published_and_hidden')
        i = 1
        if len(brains) > 0:
            for brain in brains:
                view = {}
                view['href'] = brain.getURL()
                view['title'] = brain.Title
                if self.context.absolute_url() == view['href']:
                    view['class'] = 'menutools-{} selected'.format(i)
                else:
                    view['class'] = 'menutools-{}'.format(i)
                i += 1
                menutools.append(view)
            return menutools
        else:
            return False

    def get_toolbox(self):
        view = {}
        brains = self.portal_catalog(
            object_provides=IViewletMenuToolsBox.__identifier__,
            review_state='published_and_hidden')
        if len(brains) > 0:
            brain = brains[0]
            view['href'] = brain.getURL()
            view['title'] = brain.Title
            return view
        else:
            return False
