# -*- coding: utf-8 -*-

from plone.testing import z2, Layer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE


class CpskinCoreFixture(Layer):
    defaultBases = (PLONE_FIXTURE,)


CPSKIN_CORE_FIXTURE = CpskinCoreFixture()

CPSKIN_CORE_ROBOT_TESTING = FunctionalTesting(
    bases=(CPSKIN_CORE_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name="cpskin.core:Robot")
