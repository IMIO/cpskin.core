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
     Then the view has changed


Scenario: Test folder view also on non root
    Given logged as owner
      And a folder 'simple_folder'
     When I go to 'simple_folder'
      And I open display menu
     Then the folder view with collection should be visible


Scenario: Test folder view configuration
    Given logged as owner
      And a folder 'index'
     When I go to 'index'
      And I open action menu
      And click folder view configuration
     Then the view is configured


*** Keywords ***

logged as owner
    Log in as site owner


I go to homepage
    Go to  ${PLONE_URL}


click folder view with collection
    Click Link  css=#plone-contentmenu-display-folderview


click folder view configuration
    Click Link  css=#plone-contentmenu-actions-configure_folderview


the view has changed
    Page Should Contain  View changed.


the view is configured
    Page Should Contain  Vue index avec collections configurée.
    Page Should Contain Link  css=#plone-contentmenu-display-folderview.actionMenuSelected
    Click Link  Contents
    Page Should Contain  À la une
    Page Should Contain  Actualités
    Page Should Contain  Événements
    Click Link  À la une
    Click Link  View
    Page Should Contain Link  css=#plone-contentmenu-actions-remove_from_folderview
    Page Should Not Contain Link  css=#plone-contentmenu-actions-add_to_folderview


a folder '${title}'
    Go to  ${PLONE_URL}
    Add folder  ${title}


I go to '${document_title}'
    Go to  ${PLONE_URL}/${document_title}


I open display menu
    Open Display Menu


I open action menu
    Open Action Menu


the folder view with collection should be visible
    Page Should Contain Link  css=#plone-contentmenu-display-folderview
