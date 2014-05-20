import logging
from zope.component import getAdapter
from zope.component import queryMultiAdapter
from plone import api
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import bodyfinder
from plone.app.controlpanel.security import ISecuritySchema

logger = logging.getLogger('cpskin.core')


def installCore(context):
    if context.readDataFile('cpskin.core-default.txt') is None:
        return

    logger.info('Installing')
    portal = context.getSite()
    frontPage = getattr(portal, 'front-page', None)
    setPageText(portal, frontPage, 'cpskin-frontpage-setup')


def configureMembers(context):
    if context.readDataFile('cpskin.core-membersconfig.txt') is None:
        return

    logger.info('Configuring members')
    portal = context.getSite()

    pm = getToolByName(portal, 'portal_membership')
    if not pm.getMemberareaCreationFlag():
        pm.setMemberareaCreationFlag()

    # Add a citizen group
    api.group.create('citizens', title='Citizens')

    security = getAdapter(portal, ISecuritySchema)
    # Activate Members folders
    security.set_enable_user_folders(True)
    # Activate anonymous registration
    security.set_enable_self_reg(True)

    # Clean user interface
    members = portal['Members']
    members.manage_permission('Sharing page: Delegate roles',
                              ('Manager', 'Site Administrator', 'Reviewer'),
                              acquire=0)
    members.manage_permission('Modify view template',
                              ('Manager', 'Site Administrator', 'Reviewer'),
                              acquire=0)
    members.manage_permission('Review portal content',
                              ('Manager', 'Site Administrator', 'Reviewer'),
                              acquire=0)
    members.manage_permission('Modify constrain types',
                              ('Manager', 'Site Administrator', 'Reviewer'),
                              acquire=0)

    if not members.hasObject('help-page'):
        # add Members help page
        helpPage = api.content.create(container=members, type='Document',
                                      id='help-page',
                                      title="Bienvenue dans l'espace citoyen")
        # needed because of https://github.com/plone/plone.api/issues/99
        helpPage.setTitle("Bienvenue dans l'espace citoyen")
        setPageText(portal, helpPage, 'cpskin-helppage-setup')
        members.setDefaultPage('help-page')
        # we set locally allowed types at the first configuration
        members.setConstrainTypesMode(1)
        members.setLocallyAllowedTypes(['Event'])
        members.setImmediatelyAddableTypes(['Event'])


def setPageText(portal, page, viewName):
    if page is None:
        return
    request = getattr(portal, 'REQUEST', None)
    if request is not None:
        view = queryMultiAdapter((portal, request), name=viewName)
        if view is not None:
            text = bodyfinder(view.index()).strip()
            page.setText(text, mimetype='text/html')
            page.reindexObject()
