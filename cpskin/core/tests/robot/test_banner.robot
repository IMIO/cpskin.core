*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Test enabling / disabling banner on Plone site and sub folder
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    Add folder  Subfolder
    Go to  ${PLONE_URL}/subfolder
    Add folder  SubSubfolder
    Go to  ${PLONE_URL}/subfolder
    Click Action by id  enable_banner
    Page Should Contain Element  css=#cpskin-banner
    Open Action Menu
    Element Should not be visible  css=#plone-contentmenu-actions-enable_banner
    Element Should be visible  css=#plone-contentmenu-actions-disable_banner
    Go to  ${PLONE_URL}/subfolder/subsubfolder
    Page Should Contain Element  css=#cpskin-banner
    Go to  ${PLONE_URL}
    Page Should Not Contain Element  css=#cpskin-banner
    Open Action Menu
    Element Should be visible  css=#plone-contentmenu-actions-enable_banner
    Element Should not be visible  css=#plone-contentmenu-actions-disable_banner
    Go to  ${PLONE_URL}/subfolder
    Click Action by id  disable_banner
    Page Should Not Contain Element  css=#cpskin-banner

Test enabling / disabling local banner on Plone site
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    Add folder  Subfolder
    Go to  ${PLONE_URL}/subfolder
    Add folder  SubSubfolder
    Go to  ${PLONE_URL}/subfolder
    Click Action by id  enable_local_banner
    Page Should Contain Element  css=#cpskin-banner
    Open Action Menu
    Element Should not be visible  css=#plone-contentmenu-actions-enable_local_banner
    Element Should be visible  css=#plone-contentmenu-actions-disable_local_banner
    Go to  ${PLONE_URL}/subfolder/subsubfolder
    Page Should Not Contain Element  css=#cpskin-banner
    Go to  ${PLONE_URL}
    Page Should Not Contain Element  css=#cpskin-banner
    Open Action Menu
    Element Should be visible  css=#plone-contentmenu-actions-enable_local_banner
    Element Should not be visible  css=#plone-contentmenu-actions-disable_local_banner
    Go to  ${PLONE_URL}/subfolder
    Click Action by id  disable_local_banner
    Page Should Not Contain Element  css=#cpskin-banner
