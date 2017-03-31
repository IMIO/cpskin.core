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
    Create content  type=News Item  id=$actu  title=actu
    Go to  ${PLONE_URL}/actu
    Click Link  Edit
    Sleep  1
    Click Link  Categorization
    Element Should be visible  css=#form-widgets-ISticky-sticky
