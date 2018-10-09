
# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s cpskin.core -t test_top_menu.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path cpskin cpskin.core.testing.CPSKIN_CORE_ROBOT_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot cpskin/core/tests/robot/test_top_menu.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Test Control panel content selection
    Enable autologin as  Manager
    Go to  ${PLONE_URL}
    Page should contain element  css=#top-menu-actions
    Page should not contain element  css=#top-menu-actions .top-menu-action
    ${folder}=  Create content  id=folder  type=Folder  title=Folder
    Go to  ${PLONE_URL}/folder
    Exclude from navigation
    ${foldernav}=  Create content  id=foldernav  type=Folder  title=Foldernav
    Go to  ${PLONE_URL}/plone_control_panel
    Page should contain link  @@cpskin-controlpanel
    Click link  @@cpskin-controlpanel
    Select From List By Label   xpath=//select[@id="form.contents_in_action_menu"]    Folder
    Click Button  Save
    Page should contain element  css=#top-menu-actions .top-menu-action
    Page should contain element  css=#top-menu-folder


*** Keywords ***

Exclude from navigation
    Click Link  Edit
    Click Link  id=fieldsetlegend-settings
    Select Checkbox  id=form-widgets-IExcludeFromNavigation-exclude_from_nav-0
    Click Button  Save
