# -*- coding: utf-8 -*-
import random

from Acquisition import aq_inner
from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter


HAS_MINISITE = False
try:
    from cpskin.minisite.interfaces import IInMinisite
    from cpskin.minisite.interfaces import IInPortal
    HAS_MINISITE = True
except ImportError:
    pass


class CPSkinBannerViewlet(ViewletBase):
    render = ViewPageTemplateFile('banner.pt')

    def available(self):
        context = self.context
        banner_view = getMultiAdapter((context, self.request),
                                      name="banner_activation")
        return banner_view.is_enabled

    def isInMinisite(self):
        if not HAS_MINISITE:
            return False
        return (self.isInMinisiteMode() or self.isInPortalMode())

    def show_slogan(self):
        portal_registry = api.portal.get_tool('portal_registry')
        show_slogan = portal_registry[
            'cpskin.core.interfaces.ICPSkinSettings.show_slogan']
        return show_slogan

    def slogan(self):
        default = {
            'title': "",
            'description': "",
        }
        if not self.isHomepage():
            return default
        banner = self.getBanner()
        if not banner:
            return default
        return {
            'title': banner.Title(),
            'description': banner.Description(),
        }

    def homeUrl(self):
        """
        Returns URL of :
         - object where banner was activated if not in a minisite
         - minisite root object if in a minisite
        """
        context = self.context
        request = self.request
        if not HAS_MINISITE or not self.isInMinisite():
            banner_view = getMultiAdapter((context, request),
                                          name="banner_activation")
            return banner_view.banner_root.absolute_url()
        else:
            portal = api.portal.get()
            minisite = request.get('cpskin_minisite', None)
            minisiteRoot = portal.unrestrictedTraverse(minisite.search_path)
            return minisiteRoot.absolute_url()

    def isHomepage(self):
        if self.isInMinisite():
            return False
        obj = aq_inner(self.context)
        return INavigationRoot.providedBy(obj)

    def isInMinisiteMode(self):
        if not HAS_MINISITE:
            return False
        request = self.request
        return IInMinisite.providedBy(request)

    def isInPortalMode(self):
        if not HAS_MINISITE:
            return False
        request = self.request
        return IInPortal.providedBy(request)

    def getBanner(self):
        context = self.context
        banner_folder = getattr(context, 'banner', None)
        banner = getattr(context, 'banner.jpg', None)
        if banner_folder:
            images = api.content.find(
                context=banner_folder,
                portal_type='Image',
            )
            if images:
                banner = images[random.randrange(len(images))]
                return banner.getObject()
        return banner

    def getImageBannerUrl(self):
        banner = self.getBanner()
        return banner and banner.absolute_url() or ''
