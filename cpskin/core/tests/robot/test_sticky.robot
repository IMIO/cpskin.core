*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Test that sticky field is present
    Log in as site owner
    Go to  ${PLONE_URL}
    Add news item  actu
    Go to  ${PLONE_URL}/actu
    Click Link  Edit
    Click Link  Categorization
    Element Should be visible  css=#archetypes-fieldname-sticky
