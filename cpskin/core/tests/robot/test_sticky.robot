*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Test that sticky field is present
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
    Add news item  actu
    Go to  ${PLONE_URL}/actu
    Click Link  Edit
    Click Link  Categorization
    Element Should be visible  css=#archetypes-fieldname-sticky
