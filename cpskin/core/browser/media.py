# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.Five.browser import BrowserView
from plone import api
from zope.component import getMultiAdapter
from zope.interface import alsoProvides
from zope.interface import implements
from zope.interface import noLongerProvides

from cpskin.locales import CPSkinMessageFactory as _

from cpskin.core.interfaces import IMediaActivated
from cpskin.core.browser.interfaces import IMediaActivationView


class MediaActivationView(BrowserView):
    """
    Media activation helper view
    """
    implements(IMediaActivationView)

    def _redirect(self, msg=''):
        if self.request:
            if msg:
                api.portal.show_message(message=msg,
                                        request=self.request,
                                        type='info')
            self.request.response.redirect(self.context.absolute_url())
        return msg

    def _get_real_context(self):
        context = self.context
        plone_view = getMultiAdapter((context, self.request), name="plone")
        if plone_view.isDefaultPageInFolder():
            context = aq_parent(context)
        context = aq_inner(context)
        return context

    @property
    def is_enabled(self):
        # LATER : add caching here
        context = self._get_real_context()
        if IMediaActivated.providedBy(context):
            return True
        return False

    @property
    def can_enable_media(self):
        return not self.is_enabled

    @property
    def can_disable_media(self):
        context = self._get_real_context()
        return(IMediaActivated.providedBy(context))

    def enable_media(self):
        """ Enable the media """
        context = self._get_real_context()
        alsoProvides(context, IMediaActivated)
        catalog = api.portal.get_tool('portal_catalog')
        catalog.reindexObject(context)
        self._redirect(_(
            u'Mutliamedia viewlet enabled on content and sub-contents'
        ))

    def disable_media(self):
        """ Disable the banner """
        context = self._get_real_context()
        noLongerProvides(context, IMediaActivated)
        catalog = api.portal.get_tool('portal_catalog')
        catalog.reindexObject(context)
        self._redirect(_(
            u'Mutliamedia viewlet disabled for content and sub-contents'))
