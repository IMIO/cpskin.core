# -*- coding: utf-8 -*-

from plone.testing import z2
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import cpskin.core


class CPSkinCorePloneWithPackageLayer(PloneWithPackageLayer):
    """
    """

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cpskin.core:testing')
        footer_static = portal['footer-static']
        footer_static.setText('Footer static custom content')


CPSKIN_CORE_FIXTURE = CPSkinCorePloneWithPackageLayer(
    name="CPSKIN_CORE_FIXTURE",
    zcml_filename="testing.zcml",
    zcml_package=cpskin.core,
    gs_profile_id="cpskin.core:testing")

CPSKIN_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CPSKIN_CORE_FIXTURE,),
    name="cpskin.core:Integration")

CPSKIN_CORE_ROBOT_TESTING = FunctionalTesting(
    bases=(CPSKIN_CORE_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name="cpskin.core:Robot")
