import logging
from zope.component import getAdapter
from zope.component import queryMultiAdapter
from plone import api
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import bodyfinder
from plone.app.controlpanel.security import ISecuritySchema

logger = logging.getLogger('cpskin.core')

# The profile id of your package:
PROFILE_ID = 'profile-cpskin.core:default'


def installCore(context):
    if context.readDataFile('cpskin.core-default.txt') is None:
        return

    logger.info('Installing')
    portal = context.getSite()

    # Add the MaildropHost if possible
    addMaildropHost(portal)

    # Edit front page
    frontPage = getattr(portal, 'front-page', None)
    setPageText(portal, frontPage, 'cpskin-frontpage-setup')

    # Add the Editor role to the Manage portlet permission
    portal.manage_permission('Portlets: Manage portlets',
                             ('Editor', 'Manager', 'Site Administrator'),
                             acquire=1)


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
    """
    Sets text of a Plone document if it exists and reindex the document
    The text is coming from a browser view template <body> tag
    """
    if page is None:
        return
    request = getattr(portal, 'REQUEST', None)
    if request is not None:
        view = queryMultiAdapter((portal, request), name=viewName)
        if view is not None:
            text = bodyfinder(view.index()).strip()
            page.setText(text, mimetype='text/html')
            page.reindexObject()


def addMaildropHost(self):
    """
     Add a MaildropHost if Products.MaildropHost is available...
     If MaildropHost exist, PloneGazette will use it to send mails.
     This will avoid duplicate emails send as reported by
    """
    portal = getToolByName(self, 'portal_url').getPortalObject()
    if not hasattr(portal, "MaildropHost"):
        try:
            portal.manage_addProduct['MaildropHost'].manage_addMaildropHost('MaildropHost', title='MaildropHost')
        except AttributeError:
            # if MaildropHost is not available, we pass...
            pass


def add_catalog_indexes(context):
    """Method to add our wanted indexes to the portal_catalog.

    @parameters:

    When called from the import_various method below, 'context' is
    the plone site and 'logger' is the portal_setup logger.  But
    this method can also be used as upgrade step, in which case
    'context' will be portal_setup and 'logger' will be None.


    Run the catalog.xml step as that may have defined new metadata
    columns.  We could instead add <depends name="catalog"/> to
    the registration of our import step in zcml, but doing it in
    code makes this method usable as upgrade step as well.  Note that
    this silently does nothing when there is no catalog.xml, so it
    is quite safe.
    """
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')

    catalog = getToolByName(context, 'portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')
    wanted = (('hiddenTags', 'KeywordIndex'),
              )
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def import_various(context):
    """Import step for configuration that is not handled in xml files.
    """
    # Only run step if a flag file is present
    if context.readDataFile('cpskin.core-default.txt') is None:
        return
    site = context.getSite()
    add_catalog_indexes(site)
