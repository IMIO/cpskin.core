# -*- coding: utf-8 -*-

from plone.testing import z2
from plone.app.testing import FunctionalTesting
from plone.app.testing import PloneWithPackageLayer
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import cpskin.core


CPSKIN_CORE_FIXTURE = PloneWithPackageLayer(
    name="CPSKIN_CORE_FIXTURE",
    zcml_filename="testing.zcml",
    zcml_package=cpskin.core,
    gs_profile_id="cpskin.core:testing")


CPSKIN_CORE_ROBOT_TESTING = FunctionalTesting(
    bases=(CPSKIN_CORE_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name="cpskin.core:Robot")
