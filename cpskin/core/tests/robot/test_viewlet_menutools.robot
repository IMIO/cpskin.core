*** Settings ***
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Suite Setup
Suite Teardown  Close all browsers


*** Test Cases ***
Box tools is in a overlay
    Go to  ${PLONE_URL}
    Click link  id=menutoolsbox
    Element Should Be Visible  css=div.overlay-ajax 
    
*** Keywords ***
Suite Setup
    Open test browser
    Enable autologin as  Manager
