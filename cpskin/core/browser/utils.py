# -*- coding: utf-8 -*-

from Acquisition import aq_parent
from Products.CMFPlone.utils import isDefaultPage
from Products.Five import BrowserView
from collective.folderishtypes.interfaces import IFolderishType
from plone import api


class UtilsView(BrowserView):

    def is_gdpr(self):
        return api.portal.get_registry_record(
            'imio.gdpr.interfaces.IGDPRSettings.is_text_ready',
            default=False)

    def has_folderish_default(self):
        if not IFolderishType.providedBy(self.context):
            return False
        return isDefaultPage(self.context, self.request)

    def convert_default_url(self, url, to_parent=False):
        """Converts url from default view url to parent or vice versa
        """
        obj_url = self.context.absolute_url()
        parent_url = aq_parent(self.context).absolute_url()
        if to_parent and obj_url in url:
            return url.replace(obj_url, parent_url)
        if not to_parent and obj_url not in url:
            return url.replace(parent_url, obj_url)
        return url
