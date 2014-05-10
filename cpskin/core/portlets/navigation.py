from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.interface import implements
from zope import schema
from zope.formlib import form
from plone.memoize.instance import memoize

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from plone.app.layout.navigation.navtree import buildFolderTree
from plone.app.layout.navigation.interfaces import INavtreeStrategy
from plone.app.layout.navigation.interfaces import INavigationQueryBuilder
from plone.app.portlets.portlets import navigation

from cpskin.locales import CPSkinMessageFactory as _


class ICPSkinNavigationPortlet(navigation.INavigationPortlet):
    """
      A portlet
      It inherits from IPortletDataProvider because for this portlet, the
      data that is being rendered and the portlet assignment itself are the
      same.
    """
    dropdown = schema.Bool(
        title=_(u"label_display_as_dropdown", default=u"Display as dropdown"),
        description=_(u"help_display_as_dropdown",
                        default=u"Should the navigation be displayed as a dropdown or not?  "
                                  "If not, this will be displayed as a tree (this is the default behaviour)."),
        default=False,
        required=False)


class Assignment(navigation.Assignment):
    """
      Portlet assignment
    """
    implements(ICPSkinNavigationPortlet)

    name = _(u"CPSkin")
    root = None
    currentFolderOnly = False
    includeTop = False
    topLevel = 1
    bottomLevel = 0
    dropdown = False

    def __init__(self, name=u"", root=None, currentFolderOnly=False, includeTop=False, topLevel=1, bottomLevel=0, dropdown=False):
        self.name = name
        self.root = root
        self.currentFolderOnly = currentFolderOnly
        self.includeTop = includeTop
        self.topLevel = topLevel
        self.bottomLevel = bottomLevel
        self.dropdown = dropdown


class Renderer(navigation.Renderer):
    """
      This is the customized renderer for navigation portlet
    """
    _template = ViewPageTemplateFile('navigation.pt')

    def useDropdown(self):
        return self.data.dropdown or False

    @memoize
    def getNavTree(self, _marker=[]):
        context = aq_inner(self.context)

        # Special case - if the root is supposed to be pruned, we need to
        # abort here

        queryBuilder = getMultiAdapter((context, self.data), INavigationQueryBuilder)
        strategy = getMultiAdapter((context, self.data), INavtreeStrategy)

        query = queryBuilder()
        if self.data.dropdown:
            query['path']['navtree'] = self.data.bottomLevel
            query['path']['depth'] = self.data.bottomLevel
            # if we use dropdown, look x bottomLevels under (keeping the nav strategy)
            if self.data.bottomLevel == 0:
                # infinite depth
                query['path']['depth'] = 99
            else:
                query['path']['depth'] = self.data.bottomLevel + self.data.topLevel + query['path']['navtree']
            # if the root is the portal, correct...  We search from the root defined in the portlet
            if not self.data.root:
                query['path']['query'] = ''
            else:
                query['path']['query'] = '/'.join(self.getNavRoot().getPhysicalPath())

        return buildFolderTree(context, obj=context, query=query, strategy=strategy)


class AddForm(navigation.AddForm):
    """
    """
    form_fields = form.Fields(ICPSkinNavigationPortlet)
    form_fields['root'].custom_widget = UberSelectionWidget
    label = _(u"Add CPSkin Navigation Portlet")
    description = _(u"This portlet display a navigation as tree or dropdown.")

    def create(self, data):
        return Assignment(name=data.get('name', u""),
                          root=data.get('root', u""),
                          currentFolderOnly=data.get('currentFolderOnly', False),
                          includeTop=data.get('includeTop', False),
                          topLevel=data.get('topLevel', 0),
                          bottomLevel=data.get('bottomLevel', 0),
                          dropdown=data.get('dropdown', False))


class EditForm(navigation.EditForm):
    """
    """
    form_fields = form.Fields(ICPSkinNavigationPortlet)
    form_fields['root'].custom_widget = UberSelectionWidget
    label = _(u"Edit CPSkin Navigation Portlet")
    description = _(u"This portlet display a navigation as tree or dropdown.")
