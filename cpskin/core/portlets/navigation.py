from zope.component import adapts
from zope.interface import implements
from zope.interface import Interface
from plone import api
from plone.memoize.instance import memoize
from plone.app.layout.navigation.interfaces import INavigationQueryBuilder
from plone.app.layout.navigation.interfaces import INavtreeStrategy
from plone.app.portlets.portlets.navigation import INavigationPortlet
from plone.app.portlets.portlets.navigation import NavtreeStrategy
from plone.app.portlets.portlets.navigation import QueryBuilder
from plone.app.portlets.portlets.navigation import Renderer
from plone.app.portlets.portlets.navigation import getRootPath
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from cpskin.minisite.interfaces import IInMinisiteBase
from cpskin.minisite.browser.interfaces import IHNavigationActivated
from cpskin.minisite.utils import (
    get_minisite_navigation_level,
    get_minisite_object)
HAS_MENU = False
try:
    from cpskin.menu.interfaces import IFourthLevelNavigation
    HAS_MENU = True
except ImportError:
    pass


def calculateTopLevel(context, portlet, request=None):
    """Calculate top level of navigation menu to take care of 4th level menu
    NB : IFourthLevelNavigation is activated on the third level folder
    """
    if portlet.topLevel != 3 or not HAS_MENU:
        return portlet.topLevel
    portal = api.portal.get()
    contextPhyPath = context.getPhysicalPath()
    portalPhyPath = portal.getPhysicalPath()
    path = [elem for elem in list(contextPhyPath) if elem not in list(portalPhyPath)]
    depth = len(path)
    if depth >= 3:
        subLevels = depth - 3
        if subLevels:
            thirdLevelPath = '/'.join(contextPhyPath[:-subLevels])
        else:
            thirdLevelPath = '/'.join(contextPhyPath)
        thirdLevelFolder = portal.unrestrictedTraverse(thirdLevelPath)
        if IFourthLevelNavigation.providedBy(thirdLevelFolder):
            return 4
        if request:
            if IInMinisiteBase.providedBy(request):
                minisite_obj = get_minisite_object(request)
                if minisite_obj and IHNavigationActivated.providedBy(minisite_obj):
                    return get_minisite_navigation_level(minisite_obj) + 1
    return portlet.topLevel


class CPSkinQueryBuilder(QueryBuilder):
    implements(INavigationQueryBuilder)
    adapts(Interface, INavigationPortlet)

    def __call__(self):
        topLevel = calculateTopLevel(self.context, self.portlet)
        self.query['path']['navtree_start'] = topLevel + 1
        return self.query


class CPSkinNavtreeStrategy(NavtreeStrategy):
    implements(INavtreeStrategy)
    adapts(Interface, INavigationPortlet)

    def __init__(self, context, portlet):
        NavtreeStrategy.__init__(self, context, portlet)
        portal_properties = getToolByName(context, 'portal_properties')
        navtree_properties = getattr(portal_properties, 'navtree_properties')
        currentFolderOnly = portlet.currentFolderOnly or \
            navtree_properties.getProperty('currentFolderOnlyInNavtree', False)
        topLevel = calculateTopLevel(context, portlet, context.REQUEST)

        self.rootPath = getRootPath(context, currentFolderOnly, topLevel, portlet.root)


class CPSkinRenderer(Renderer):
    _template = ViewPageTemplateFile('navigation.pt')

    @memoize
    def getNavRootPath(self):
        currentFolderOnly = self.data.currentFolderOnly or \
            self.properties.getProperty('currentFolderOnlyInNavtree', False)

        topLevel = calculateTopLevel(self.context, self.data, self.request)
        root = self.data.root
        if isinstance(root, unicode):
            root = str(root)

        return getRootPath(self.context, currentFolderOnly, topLevel, root)
