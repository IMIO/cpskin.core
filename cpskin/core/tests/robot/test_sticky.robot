
# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s cpskin.core -t test_sticky.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path cpskin cpskin.core.testing.CPSKIN_CORE_ROBOT_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot -i current cpskin/core/tests/robot/test_sticky.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Test that sticky field is present
    [Tags]  current
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    ${folder_uid}  Create content  type=Folder  id=folder  title=folder
    Create content  type=News Item  container=${folder_uid}  id=$actu  title=actu
    Go to  ${PLONE_URL}/folder/actu
    Click Link  Edit
    Sleep  1
    Click Link  Categorization
    Element Should be visible  css=#form-widgets-ISticky-sticky
