*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Scenario: Test folder view with collection
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    ${folder_uid}  Create content  type=Folder  id=simple_folder  title=simple_folder
    Open Display Menu
    Click Link  css=#plone-contentmenu-display-folderview
    Page Should Contain  View changed.


Scenario: Test folder view also on non root
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    ${folder_uid}  Create content  type=Folder  id=simple_folder  title=simple_folder
    Go to  ${PLONE_URL}/simple_folder
    Open Display Menu
    Page Should Contain Link  css=#plone-contentmenu-display-folderview


Scenario: Test folder view configuration
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    ${folder_uid}  Create content  type=Folder  id=index  title=index
    Go to  ${PLONE_URL}/index
    Open Menu  plone-contentmenu-cpskin-configurations
    Click Link  css=#plone-contentmenu-cpskin-configurations-configure_folderview
    Wait until keyword succeeds  3  1  Page Should Contain  Vue index avec collections configurée.
    Page Should Contain Link  css=#plone-contentmenu-display-folderview.actionMenuSelected
    Click Link  Contents
    Page Should Contain  À la une
    Page Should Contain  Actualités
    Page Should Contain  Événements
    Click Link  À la une
    Sleep  1
    Click Link  View
    Page Should Contain Link  css=#plone-contentmenu-cpskin-configurations-remove_from_folderview
    Page Should Not Contain Link  css=#plone-contentmenu-cpskin-configurations-add_to_folderview
