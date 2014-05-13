# -*- coding: utf-8 -*-
from plone.testing import layered
from cpskin.core.testing import CPSKIN_CORE_ROBOT_TESTING

import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite('robot'),
                layer=CPSKIN_CORE_ROBOT_TESTING),
    ])
    return suite
