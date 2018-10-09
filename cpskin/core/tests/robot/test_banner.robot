
# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s cpskin.core -t test_banner.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path cpskin cpskin.core.testing.CPSKIN_CORE_ROBOT_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot cpskin/core/tests/robot/test_banner.robot
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

Test enabling / disabling banner on Plone site and sub folder
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    ${folder_uid}  Create content  type=Folder  title=Subfolder
    Go to  ${PLONE_URL}/subfolder
    Create content  type=Folder  container=${folder_uid}  title=SubSubfolder
    Go to  ${PLONE_URL}/subfolder
    Click CPSkin Configuration by id  enable_banner
    Page Should Contain Element  css=#cpskin-banner
    Open CPSkin Configuration Menu
    Element Should not be visible  css=#plone-contentmenu-cpskin-configurations-enable_banner
    Element Should be visible  css=#plone-contentmenu-cpskin-configurations-disable_banner
    Go to  ${PLONE_URL}/subfolder/subsubfolder
    Page Should Contain Element  css=#cpskin-banner
    Go to  ${PLONE_URL}
    Page Should Not Contain Element  css=#cpskin-banner
    Open CPSkin Configuration Menu
    Element Should be visible  css=#plone-contentmenu-cpskin-configurations-enable_banner
    Element Should not be visible  css=#plone-contentmenu-cpskin-configurations-disable_banner
    Go to  ${PLONE_URL}/subfolder
    Click CPSkin Configuration by id  disable_banner
    # Sleep  1
    Page Should Not Contain Element  css=#cpskin-banner


Test enabling / disabling local banner on Plone site
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    ${folder_uid}  Create content  type=Folder  id=subfolder  title=Subfolder
    Go to  ${PLONE_URL}/subfolder
    Create content  type=Folder  container=${folder_uid}  id=subSubfolder  title=SubSubfolder
    Go to  ${PLONE_URL}/subfolder
    Click CPSkin Configuration by id  enable_local_banner
    Page Should Contain Element  css=#cpskin-banner
    Open CPSkin Configuration Menu
    Element Should not be visible  css=#plone-contentmenu-cpskin-configurations-enable_local_banner
    Element Should be visible  css=#plone-contentmenu-cpskin-configurations-disable_local_banner
    Go to  ${PLONE_URL}/subfolder/subsubfolder
    Page Should Not Contain Element  css=#cpskin-banner
    Go to  ${PLONE_URL}
    Page Should Not Contain Element  css=#cpskin-banner
    Open CPSkin Configuration Menu
    Element Should be visible  css=#plone-contentmenu-cpskin-configurations-enable_local_banner
    Element Should not be visible  css=#plone-contentmenu-cpskin-configurations-disable_local_banner
    Go to  ${PLONE_URL}/subfolder
    Click CPSkin Configuration by id  disable_local_banner
    # Sleep  1
    Page Should Not Contain Element  css=#cpskin-banner


*** Keywords ***

Open CPSkin Configuration Menu
    Open Menu  plone-contentmenu-cpskin-configurations

Click CPSkin Configuration by id
    [arguments]  ${name}

    Open CPSkin Configuration Menu
    Element Should be visible  css=dl#plone-contentmenu-cpskin-configurations dd.actionMenuContent  #plone-contentmenu-cpskin-configurations-${name}
    Click Link  id=plone-contentmenu-cpskin-configurations-${name}
