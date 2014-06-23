# -*- coding: utf-8 -*-

from plone import api
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IFolderish

from cpskin.locales import CPSkinMessageFactory as _


class FolderView(BrowserView):

    def can_configure(self):
        """
        Check if folderview can be configured on context
        """
        context = self.context
        if not IFolderish.providedBy(context):
            return False
        layout = context.getLayout()
        if layout != 'folderview':
            return True
        return False

    def configure(self):
        """
        Configure folders and collections for folderview
        """
        context = self.context
        existingIds = context.objectIds()
        portalPath = api.portal.get().getPhysicalPath()
        contextPath = '/'.join(context.getPhysicalPath()[len(portalPath)])
        if 'a-la-une' not in existingIds:
            folder = api.content.create(container=context,
                                        type='Folder',
                                        id='a-la-une',
                                        title="À la une")
            collection = api.content.create(container=folder,
                                            type='Collection',
                                            id='a-la-une',
                                            title="À la une")
            query = [{'i': 'HiddenTags',
                      'o': 'plone.app.querystring.operation.selection.is',
                      'v': 'a-la-une'},
                      {'i': 'path',
                      'o': 'plone.app.querystring.operation.string.path',
                      'v': '/%s' % contextPath}]
            collection.setQuery(query)
            collection.setSort_on('effective')
            collection.setSort_reversed(True)
            collection.setLayout('folder_summary_view')
            folder.setDefaultPage('a-la-une')
        if 'actualites' not in existingIds:
            folder = api.content.create(container=context,
                                        type='Folder',
                                        id='actualites',
                                        title="Actualités")
            collection = api.content.create(container=folder,
                                            type='Collection',
                                            id='actualites',
                                            title="Actualités")
            query = [{'i': 'portal_type',
                      'o': 'plone.app.querystring.operation.selection.is',
                      'v': ['News Item']},
                      {'i': 'path',
                      'o': 'plone.app.querystring.operation.string.path',
                      'v': '/%s' % contextPath}]
            collection.setQuery(query)
            collection.setSort_on('effective')
            collection.setSort_reversed(True)
            collection.setLayout('folder_summary_view')
            folder.setDefaultPage('actualites')
        if 'evenements' not in existingIds:
            folder = api.content.create(container=context,
                                        type='Folder',
                                        id='evenements',
                                        title="Événements")
            collection = api.content.create(container=folder,
                                            type='Collection',
                                            id='evenements',
                                            title="Événements")
            query = [{'i': 'portal_type',
                      'o': 'plone.app.querystring.operation.selection.is',
                      'v': ['Event']},
                      {'i': 'path',
                      'o': 'plone.app.querystring.operation.string.path',
                      'v': '/%s' % contextPath}]
            collection.setQuery(query)
            collection.setSort_on('effective')
            collection.setSort_reversed(True)
            collection.setLayout('folder_summary_view')
            folder.setDefaultPage('evenements')

        context.setLayout('folderview')
        api.portal.show_message(message=_(u"Vue index avec collections configurée."),
                                request=self.request,
                                type='info')
        self.request.response.redirect(context.absolute_url())
        return ''

    def getNews(self, navigation_root_path):
        path = '/'.join([navigation_root_path, 'actualites'])
        return self.searchCollection(path)

    def getEvents(self, navigation_root_path):
        path = '/'.join([navigation_root_path, 'evenements'])
        return self.searchCollection(path)

    def searchCollection(self, path):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        queryDict = {}
        queryDict['path'] = {'query': path, 'depth': 1}
        queryDict['portal_type'] = 'Collection'
        queryDict['sort_limit'] = 1
        collections = portal_catalog.searchResults(queryDict)
        return collections and collections[0] or None

    def getFrontPageText(self):
        frontPage = getattr(self.context, 'front-page', None)
        if frontPage is None:
            return
        if frontPage.Language() == self.context.Language():
            return frontPage.getText()
        if hasattr(frontPage, 'getTranslation'):
            lang = self.context.REQUEST.get('LANGUAGE', 'fr')
            frontPage = frontPage.getTranslation(lang)
        return frontPage.getText()

    def hasFlexSlider(self):
        """
        Check if flexslider is available and installed
        """
        try:
            from cpskin.slider.interfaces import ICPSkinSliderLayer
        except ImportError:
            return False
        else:
            request = getattr(self.context, "REQUEST", None)
            if ICPSkinSliderLayer.providedBy(request):
                return True
            return False

    def getSliderContent(self):
        container = getattr(self.context, 'a-la-une', None)
        if container is None:
            return []
        return container.queryCatalog()
