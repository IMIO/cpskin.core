from zope.component import getMultiAdapter
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

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

    def homeUrl(self):
        if not HAS_MINISITE:
            return None
        request = self.request
        portal = api.portal.get()
        minisite = request.get('cpskin_minisite', None)
        minisiteRoot = portal.unrestrictedTraverse(minisite.search_path)
        return minisiteRoot.absolute_url()

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
