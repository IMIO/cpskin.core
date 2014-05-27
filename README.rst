.. contents::

Introduction
============

Core package for cpskin


Tests
=====

This package is tested using Travis CI. The current status is :

.. image:: https://travis-ci.org/IMIO/cpskin.core.png
    :target: http://travis-ci.org/IMIO/cpskin.core


Robot tests
===========


Run all tests
-------------

bin/test


Run specific tests
------------------

You can launch the robot server with the command:

    bin/robot-server cpskin.core.testing.CPSKIN_CORE_ROBOT_TESTING

And launch the tests:

    bin/robot cpskin/core/tests/robot/<yourfile>.robot

You can sandbox on http://localhost:55001/plone/
