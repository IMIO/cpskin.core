*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Variables ***


*** Test cases ***


Test static footer visible
    Page Should Contain  Footer static custom content

Test edit static footer
    Log in as site owner
    Page Should Contain Element  css=div.footer-static >p >a
    Click element  css=div.footer-static >p >a
    Location Should Be  http://localhost:55001/plone/footer-static/edit
