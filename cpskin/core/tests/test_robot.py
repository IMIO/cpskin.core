# -*- coding: utf-8 -*-
from plone.testing import layered
from cpskin.core.testing import CPSKIN_CORE_ROBOT_TESTING

import os
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    robot_dir = os.path.join(current_dir, 'robot')
    robot_tests = [
        os.path.join('robot', doc) for doc in
        os.listdir(robot_dir) if doc.endswith('.robot') and
        doc.startswith('test_')
    ]
    for robot_test in robot_tests:
        robottestsuite = robotsuite.RobotTestSuite(robot_test)
        suite.addTests([
            layered(
                robottestsuite,
                layer=CPSKIN_CORE_ROBOT_TESTING
            ),
        ])
    return suite
