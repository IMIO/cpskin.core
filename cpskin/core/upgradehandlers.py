# -*- coding: utf-8 -*-
from Acquisition import aq_get
from cpskin.core.behaviors.eventview import ICpskinEventViewSettings
from cpskin.core.behaviors.indexview import ICpskinIndexViewSettings
from cpskin.core.faceted.interfaces import ICPSkinPossibleFacetedNavigable
from cpskin.core.setuphandlers import addAutoPlaySliderToRegistry
from cpskin.core.setuphandlers import addCityNameToRegistry
from cpskin.core.setuphandlers import addDescriptionOnThemesOptionToRegistry
from cpskin.core.setuphandlers import addLoadPageMenuToRegistry
from cpskin.core.setuphandlers import addMediaViewletOptionsToRegistry
from cpskin.core.setuphandlers import addPortletsInRightActionsToRegistry
from cpskin.core.setuphandlers import addShowSloganToRegistry
from cpskin.core.setuphandlers import addSliderTimerToRegistry
from cpskin.core.setuphandlers import addSliderTypeToRegistry
from cpskin.core.setuphandlers import addSubMenuPersistenceToRegistry
from cpskin.core.setuphandlers import addTopMenuContentsToRegistry
from cpskin.core.setuphandlers import addTopMenuLeadImageToRegistry
from cpskin.core.utils import add_behavior
from cpskin.core.utils import remove_behavior
from eea.facetednavigation.subtypes.interfaces import IPossibleFacetedNavigable
from plone import api
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import alsoProvides
from zope.interface import directlyProvidedBy
from zope.interface import directlyProvides

import logging


logger = logging.getLogger('cpskin.core')


def upgrade_registry_for_themes_descriptions(context):
    addDescriptionOnThemesOptionToRegistry()


def upgrade_registry_for_media_viewlet(context):
    addMediaViewletOptionsToRegistry(upgrade=True)


def add_right_actions(context):
    addPortletsInRightActionsToRegistry()
    context.runImportStepFromProfile(
        'profile-cpskin.core:default',
        'viewlets'
    )
    context.runImportStepFromProfile(
        'profile-cpskin.core:default',
        'jsregistry'
    )


def upgrade_registry_for_slogan(context):
    addShowSloganToRegistry()


def update_types(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'typeinfo')


def clean_portal_setup(context):
    """
    Force uninstall of packages that are not marked as installed but were
    imported in portal_setup : #17714
    """
    ps = api.portal.get_tool('portal_setup')
    qi = api.portal.get_tool('portal_quickinstaller')
    quick_installed = [p['id'] for p in qi.listInstalledProducts()]
    all_profiles = [p['id'] for p in context.listContextInfos() \
                    if p['type'] == 'extension']
    cpskin_profiles = [p for p in all_profiles \
                       if p.startswith('profile-cpskin.diazotheme.')]
    for profile_id in cpskin_profiles:
        if 'uninstall' in profile_id:
            continue
        if ps.getLastVersionForProfile(profile_id) == 'unknown':
            # profile is not installed
            logger.info('{0} is not installed - skipping'.format(profile_id))
            continue
        package_id = profile_id.split('-')[1].split(':')[0]
        if package_id in quick_installed:
            # profile is installed, product is also installed in quickinstaller
            logger.info('{0} is well installed - skipping'.format(profile_id))
            continue
        logger.warn('{0} is NOT installed correctly'.format(profile_id))
        uninstall_profile_id = 'profile-{0}:uninstall'.format(package_id)
        if uninstall_profile_id in all_profiles:
            # install lesscss because uninstall profiles need it.
            if not qi.isProductInstalled('collective.lesscss'):
                context.runAllImportStepsFromProfile(
                    'profile-collective.lesscss:default')
                qi.installProduct('collective.lesscss')
            context.runAllImportStepsFromProfile(uninstall_profile_id)
            ps.unsetLastVersionForProfile(profile_id)
            qi.uninstallProducts(products=[str(package_id)])
            logger.info('{0} uninstalled successfully !'.format(package_id))
        else:
            logger.warn('No uninstall profile for {0}'.format(package_id))

    psk = api.portal.get_tool('portal_skins')
    selected_skin = 'Sunburst Theme'
    if psk.default_skin != selected_skin:
        psk.default_skin = selected_skin
        request = aq_get(context, 'REQUEST', None)
        portal = api.portal.get()
        portal.changeSkin(selected_skin, request)
        logger.info('Restored default_skin : {0}'.format(selected_skin))


def upgrade_viewlets(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'viewlets')


def upgrade_registry_for_top_menu(context):
    addTopMenuContentsToRegistry()
    addTopMenuLeadImageToRegistry()


def migrate_a_la_une_sliders(context):
    brains = api.content.find(
        id="a-la-une",
        portal_type="Collection",
    )
    for brain in brains:
        obj = brain.getObject()
        obj.display_type = u'slider-with-carousel'


def update_theme_variables(context):
    context.runAllImportStepsFromProfile('profile-cpskin.theme:default')
    key = 'plone.app.theming.interfaces.IThemeSettings.parameterExpressions'
    params = {}
    params['globalnavsetting'] = "python: 'always'"
    params['isinminisitemode'] = 'context/@@isInMinisiteMode'
    params['is_homepage'] = 'context/@@is_homepage'
    params['environment'] = 'context/@@environment'
    params['login_message'] = 'context/@@get_login_message'
    api.portal.set_registry_record(key, params)


def empty_value_of_link_text(context):
    for brain in api.content.find(portal_type='Collection'):
        obj = brain.getObject()
        path = '/'.join(obj.getPhysicalPath())
        logger.info('set link_text empty for {0}'.format(path))
        setattr(obj, 'link_text', '')


def upgrade_to_nineteen(context):
    context.runImportStepFromProfile('profile-cpskin.core:to19', 'jsregistry')
    pc = api.portal.get_tool('portal_catalog')
    for brain in pc.unrestrictedSearchResults(
                    object_provides=IPossibleFacetedNavigable.__identifier__):
        obj = brain.getObject()
        if obj:
            alsoProvides(obj, ICPSkinPossibleFacetedNavigable)


def clean_old_keyword_homepage(context):
    behavior_name = 'cpskin.core.behaviors.metadata.IUseKeywordHomepage'
    types = [
        'Folder',
        'Collection',
        'Document',
        'Event',
        'News Item',
        'organization',
        'person'
    ]
    for type_name in types:
        remove_behavior(type_name, behavior_name)


def move_cpskin_actions(context):
    context.runImportStepFromProfile('profile-cpskin.core:to17', 'actions')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'actions')


def add_navigation_toggle_action(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'actions')


def add_index_view_behavior(context):
    registry = getUtility(IRegistry)
    del registry.records[
        'cpskin.core.interfaces.ICPSkinSettings.homepage_keywords']
    add_behavior('Collection', ICpskinIndexViewSettings.__identifier__)


def add_banner_view_behavior(context):
    add_behavior('Event', ICpskinEventViewSettings.__identifier__)


def upgrade_homepage_keywords(context):
    # add_homepage_keywords()
    pass


def upgrade_minisite_menu(context):
    # add new viewlet cpskin.minisite
    context.runImportStepFromProfile('profile-cpskin.core:default', 'viewlets')
    context.runImportStepFromProfile(
        'profile-cpskin.menu:default', 'jsregistry')
    context.runImportStepFromProfile(
        'profile-cpskin.minisite:default', 'actions')


def upgrade_city_name(context):
    addCityNameToRegistry()


def upgrade_slider_type(context):
    addSliderTypeToRegistry()


def upgrade_footer_viewlet(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'viewlets')


def upgrade_to_eleven(context):
    addSubMenuPersistenceToRegistry()


def upgrade_to_eight(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'rolemap')


def upgrade_to_seven(context):
    addAutoPlaySliderToRegistry()
    addSliderTimerToRegistry()


def upgrade_to_six(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'rolemap')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'sharing')
    portal = api.portal.get()
    portal.manage_permission('CPSkin: Edit keywords',
                             roles=['Portlets Manager',
                                    'Manager', 'Site Administrator'],
                             acquire=True)
    site_properties = api.portal.get_tool('portal_properties').site_properties
    site_properties.allowRolesToAddKeywords = ('Manager',
                                               'Site Administrator',
                                               'Portlets Manager')


def upgrade_to_five(context):
    interfaces = ['cpskin.core.viewlets.interfaces.IViewletMenuToolsBox',
                  'cpskin.core.viewlets.interfaces.IViewletMenuToolsFaceted']
    catalog = api.portal.get_tool('portal_catalog')
    for interface in interfaces:
        brains = catalog({'object_provides': interface})
        for brain in brains:
            obj = brain.getObject()
            provided = directlyProvidedBy(obj)
            cleanedProvided = [
                i for i in provided if i.__identifier__ != interface]
            directlyProvides(obj, cleanedProvided)  # noqa
            obj.reindexObject()

    portal_javascripts = api.portal.get_tool('portal_javascripts')
    portal_javascripts.unregisterResource(
        '++resource++cpskin.core.menutools.js')


def upgrade_to_four(context):
    addLoadPageMenuToRegistry()


def upgrade_to_three(context):
    context.runImportStepFromProfile('profile-cpskin.core:default', 'actions')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'rolemap')
    context.runImportStepFromProfile('profile-cpskin.core:default', 'sharing')
    portal = api.portal.get()
    portal.manage_permission('Portlets: Manage portlets',
                             roles=['Editor', 'Portlets Manager',
                                    'Manager', 'Site Administrator'],
                             acquire=True)


def upgrade_to_two(context):
    context.runAllImportStepsFromProfile('profile-cpskin.policy:default')
    portal_catalog = api.portal.get_tool('portal_catalog')
    portal_atct = api.portal.get_tool('portal_atct')
    attrs = ('IAmTags', 'HiddenTags', 'ISearchTags')
    for attr in attrs:
        if attr in portal_catalog.indexes():
            portal_catalog.delIndex(attr)
        if attr in portal_atct.topic_indexes:
            portal_atct.removeIndex(attr)
    for brain in portal_catalog.searchResults():  # noqa
        obj = brain.getObject()
        for attr in attrs:
            if hasattr(obj, attr):
                try:
                    delattr(obj, attr)
                except AttributeError:
                    logger.info('No {0} on: {1}'.format(attr, obj))
