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
    request = getattr(portal, 'REQUEST', None)

    frontPage = getattr(portal, 'front-page')
    if frontPage:
        if request is not None:
            view = queryMultiAdapter((portal, request),
                                     name='cpskin-frontpage-setup')
            if view is not None:
                text = bodyfinder(view.index()).strip()
                frontPage.setText(text, mimetype='text/html')


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
