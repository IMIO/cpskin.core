*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Scenario: Test folder view with collection
    Given logged as owner
     When I go to homepage
      And I open display menu
      And click folder view with collection
     Then the collections should be visible


Scenario: Test no folder view in non root
    Given logged as owner
      And a folder 'simple_folder'
     When I go to 'simple_folder'
      And I open display menu
     Then the folder view with collection should not be visible


*** Keywords ***

logged as owner
    Log in as site owner


I go to homepage
    Go to  ${PLONE_URL}


I set folder view with collection
    Go to  ${PLONE_URL}
    Open Display Menu


click folder view with collection
    Click Link  css=#plone-contentmenu-display-folderview


the collections should be visible
    Page Should Contain Link  css=a[href=actualites]
    Page Should Contain Link  css=a[href=evenements]


a folder '${title}'
    Go to  ${PLONE_URL}
    Add folder  ${title}


I go to '${document_title}'
    Go to  ${PLONE_URL}/${document_title}


I open display menu
    Open Display Menu


the folder view with collection should not be visible
    Page Should Not Contain Link  css=#plone-contentmenu-display-folderview
