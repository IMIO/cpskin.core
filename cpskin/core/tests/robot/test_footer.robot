*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Test static footer visible
    Page Should Contain  Footer static custom content

Test edit static footer
    Enable autologin as  Manager
    Go to  ${PLONE_URL}
    Page Should Contain Element  css=div.footer-static >p >a
    Click element  css=div.footer-static >p >a
    Location Should Be  ${PLONE_URL}/footer-static/edit
