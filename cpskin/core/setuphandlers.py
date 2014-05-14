import logging
from zope.component import getAdapter
from plone import api
from Products.CMFCore.utils import getToolByName
from plone.app.controlpanel.security import ISecuritySchema

logger = logging.getLogger('cpskin.core')


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
