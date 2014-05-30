*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Test enabling / disabling banner on Plone site and sub folder
    Log in as site owner
    Go to  ${PLONE_URL}
    Add folder  Subfolder
    Go to  ${PLONE_URL}/subfolder
    Click Action by id  enable_banner
    Page Should Contain Element  css=#cpskin-banner
    Open Action Menu
    Element Should not be visible  css=#plone-contentmenu-actions-enable_banner
    Element Should be visible  css=#plone-contentmenu-actions-disable_banner
    Go to  ${PLONE_URL}
    Page Should Not Contain Element  css=#cpskin-banner
    Open Action Menu
    Element Should be visible  css=#plone-contentmenu-actions-enable_banner
    Element Should not be visible  css=#plone-contentmenu-actions-disable_banner
    Go to  ${PLONE_URL}/subfolder
    Click Action by id  disable_banner
    Page Should Not Contain Element  css=#cpskin-banner
