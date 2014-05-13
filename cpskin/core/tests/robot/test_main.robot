*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers

*** Variables ***

*** Keywords ***

*** Test cases ***

Login as owner
    Log in as site owner
    Go to  ${PLONE_URL}
    Page should contain  Plone site
