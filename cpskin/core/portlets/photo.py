from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.interface import implements
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IPhotoPortlet(IPortletDataProvider):
    """
    Photo portlet interface
    """


class Assignment(base.Assignment):
    implements(IPhotoPortlet)


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('photo.pt')

    @property
    def available(self):
        """
        Portlet should be available everywhere except on root
        """
        context_state = getMultiAdapter((aq_inner(self.context), self.request),
                                        name=u'plone_context_state')
        isRoot = context_state.is_portal_root()
        if isRoot:
            return False
        return True


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
