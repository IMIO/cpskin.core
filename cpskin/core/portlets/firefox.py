from zope.interface import implements
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IFirefoxPortlet(IPortletDataProvider):
    """
    Firefox portlet interface
    """


class Assignment(base.Assignment):
    implements(IFirefoxPortlet)


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('firefox.pt')

    @property
    def available(self):
        return 'Firefox' not in self.request.get('HTTP_USER_AGENT', None)


class AddForm(base.NullAddForm):

    def create(self):
        return Assignment()
