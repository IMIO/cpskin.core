.. contents::

Introduction
============

Core package for cpskin


Tests
=====

This package is tested using Travis CI. The current status is :

.. image:: https://travis-ci.org/IMIO/cpskin.core.png
    :target: http://travis-ci.org/IMIO/cpskin.core

.. image:: https://coveralls.io/repos/github/IMIO/cpskin.core/badge.svg?branch=master
    :target: https://coveralls.io/github/IMIO/cpskin.core?branch=master

Tests
=====

Run all tests
-------------

bin/test


Run specific robot tests
------------------------

You can launch the robot server with the command::

    bin/robot-server cpskin.core.testing.CPSKIN_CORE_ROBOT_TESTING

And launch the tests::

    bin/robot cpskin/core/tests/robot/<yourfile>.robot

You can sandbox on http://localhost:55001/plone/
