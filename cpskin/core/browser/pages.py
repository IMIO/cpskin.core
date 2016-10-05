# -*- coding: utf-8 -*-
from collective.documentgenerator.browser.generation_view import DocumentGenerationView
from cpskin.core.interfaces import IFolderViewSelectedContent as IFVSC
from plone import api
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserView


class FrontPage(BrowserView):

    index = ViewPageTemplateFile('templates/frontpage.pt')


class HelpPage(BrowserView):

    index = ViewPageTemplateFile('templates/helppage.pt')


class OpenData(BrowserView):
    """Get data news, events rss feed and collective.directory csv files."""

    index = ViewPageTemplateFile('templates/opendata.pt')

    def get_links(self):
        portal = api.portal.get()
        links = []
        path = '/'.join(portal.getPhysicalPath())
        portal_catalog = api.portal.get_tool('portal_catalog')
        query_dict = {}
        query_dict['path'] = {'query': path, 'depth': 1}
        query_dict['portal_type'] = ['Folder']
        query_dict['object_provides'] = IFVSC.__identifier__
        query_dict['sort_on'] = 'getObjPositionInParent'
        brains = portal_catalog(query_dict)
        for brain in brains:
            folder = brain.getObject()
            if getattr(folder, "default_page", None):
                default_page = folder.default_page
                default_obj = folder[default_page]
                rsslink = "{0}/atom.xml".format(default_obj.absolute_url())
                links.append(rsslink)

        query_dict = {}
        query_dict['portal_type'] = ['collective.directory.directory']
        brains = portal_catalog(query_dict)
        for brain in brains:
            directory = brain.getObject()
            catalog = api.portal.get_tool('portal_catalog')
            query_dict = {}
            query_dict['portal_type'] = 'collective.directory.card'
            query_dict['path'] = {
                'query': "/".join(directory.getPhysicalPath()), 'depth': 3}
            size = len(catalog(query_dict))
            if size > 3:
                csvlink = "{0}/collective_directory_export_view".format(
                    directory.absolute_url()
                )
                links.append(csvlink)

        return links


class IDDocumentGenerationView(DocumentGenerationView):
    """Override the 'get_generation_context' properly so 'get_base_generation_context'
       is available for sub-packages that want to extend the template generation context."""

    def _get_generation_context(self, helper_view):
        view = self.context.restrictedTraverse('faceted_query')
        brains = view.query(batch=False)
        return {'brains': brains}
