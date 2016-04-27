# -*- coding: utf-8 -*-

from plone.testing import z2
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE

import cpskin.core


class CPSkinCorePloneWithPackageLayer(PloneWithPackageLayer):
    """
    """

    def setUpZope(self, app, configurationContext):
        super(CPSkinCorePloneWithPackageLayer, self).setUpZope(app, configurationContext)
        z2.installProduct(app, 'Products.DateRecurringIndex')
        # import plone.app.contenttypes
        # self.loadZCML(package=plone.app.contenttypes)
        # import plone.app.event
        # self.loadZCML(package=plone.app.event)

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.DateRecurringIndex')

    def setUpPloneSite(self, portal):
        portal.portal_workflow.setDefaultChain('simple_publication_workflow')
        # applyProfile(portal, 'plone.app.contenttypes:plone-content')
        applyProfile(portal, 'cpskin.core:testing')
        # footer_static = portal['footer-static']
        # footer_static.setText('Footer static custom content')


CPSKIN_CORE_FIXTURE = CPSkinCorePloneWithPackageLayer(
    name="CPSKIN_CORE_FIXTURE",
    zcml_filename="testing.zcml",
    zcml_package=cpskin.core,
    gs_profile_id="cpskin.core:testing")

CPSKIN_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CPSKIN_CORE_FIXTURE,),
    name="cpskin.core:Integration")

CPSKIN_CORE_ROBOT_TESTING = FunctionalTesting(
    bases=(CPSKIN_CORE_FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name="cpskin.core:Robot")
