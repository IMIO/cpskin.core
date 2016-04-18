from zope.publisher.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from cpskin.core.interfaces import IFolderViewSelectedContent as IFVSC


class FrontPage(BrowserView):

    index = ViewPageTemplateFile('templates/frontpage.pt')


class HelpPage(BrowserView):

    index = ViewPageTemplateFile('templates/helppage.pt')


class OpenData(BrowserView):
    """ Get data news, events rss feed and collective.directory csv files."""

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
        # query_dict['review_state'] = (
        #     'published_and_hidden',
        #     'published_and_shown',
        #     'published'
        # )
        brains = portal_catalog(query_dict)
        for brain in brains:
            folder = brain.getObject()
            default_page = folder.default_page
            default_obj = folder[default_page]
            rsslink = "{}/atom.xml".format(default_obj.absolute_url())
            links.append(rsslink)

        query_dict = {}
        query_dict['portal_type'] = ['collective.directory.directory']
        brains = portal_catalog(query_dict)
        for brain in brains:
            directory = brain.getObject()
            csvlink = "{}/collective_directory_export_view".format(
                directory.absolute_url()
            )
            links.append(csvlink)

        return links

