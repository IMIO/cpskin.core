# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone import api


class UtilsView(BrowserView):

    def is_gdpr(self):
        return api.portal.get_registry_record(
            'imio.gdpr.interfaces.IGDPRSettings.is_text_ready',
            default=False)
