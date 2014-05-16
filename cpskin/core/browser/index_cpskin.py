# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class IndexCPSkin(BrowserView):


    def getActualites(self, navigation_root_path):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        queryDict = {}
        queryDict['path'] = {'query': navigation_root_path, 'depth': 1}
        queryDict['portal_type'] = 'Collection'
        queryDict['Title'] = 'actualites'
        return portal_catalog.searchResults(queryDict)[0]

    def getEvenements(self, navigation_root_path):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        queryDict = {}
        queryDict['path'] = {'query': navigation_root_path, 'depth': 1}
        queryDict['portal_type'] = 'Collection'
        queryDict['Title'] = 'evenements'
        return portal_catalog.searchResults(queryDict)[0]

    def getFrontPageText(self):
        frontPage = getattr(self.context, 'front-page')
        if hasattr(frontPage, 'getTranslation'):
            frontPage = frontPage.getTranslation(context.REQUEST.get('LANGUAGE', 'fr'))
        return frontPage.getText()
