# -*- coding: utf-8 -*-
import random

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets.common import ViewletBase
from plone.namedfile.scaling import ImageScale
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

    def get_slogan(self):
        default = {
            'title': '',
            'description': '',
        }
        if not self.isFolderView():
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

    def isFolderView(self):
        context = self.context
        layout = context.getLayout()
        return (layout == 'folderview')

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
        local_banner_folder = getattr(context.aq_explicit, 'banner', None)
        local_banner_event = getattr(context.aq_explicit, 'image_banner', None)
        local_banner = getattr(context.aq_explicit, 'banner.jpg', None)
        banner_folder = getattr(context, 'banner', None)
        banner = getattr(context, 'banner.jpg', None)
        if context.portal_type == 'Event' and local_banner_event:
            banner = context.restrictedTraverse('@@images').scale(fieldname='image_banner')
            return banner
        if local_banner_folder or (banner_folder and not local_banner):
            banner_folder_to_use = local_banner_folder and local_banner_folder or banner_folder
            images = api.content.find(
                context=banner_folder_to_use,
                portal_type='Image',
            )
            if images:
                banner = images[random.randrange(len(images))]
                return banner.getObject()
        return banner

    def getImageBannerUrl(self):
        banner = self.getBanner()
        if not banner:
            return ''
        if isinstance(banner, ImageScale):
            image_scale = banner
        else:
            view = banner.restrictedTraverse('@@images')
            image_scale = view.scale('image', scale='banner')
        return image_scale.absolute_url()
