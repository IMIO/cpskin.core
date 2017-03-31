*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Scenario: Test collection hidden tags criteria
    Given logged as owner
      And a document 'simple_document' with hidden tag 'sample_keyword_accentué'
      And a collection  simple_collection
     When I set to the collection 'simple_collection' the search terms hidden tag 'sample_keyword_accentué'
     Then the collection 'simple_collection' should contain 'simple_document'


*** Keywords ***

logged as owner
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}


a document '${title}' with hidden tag '${keyword}'
    Go to  ${PLONE_URL}
    Create content  type=Document  title=${title}
    Go to  ${PLONE_URL}/${title}
    Click Edit In Edit bar
    Sleep  1
    Click Link  Categorization
    Input Text  form.widgets.IHiddenTags.hiddenTags_additional  ${keyword}
    Click Button  Save
    Element Should Contain  id=hidden-tags  ${keyword}


a collection
    [Arguments]  ${title}
    Go to  ${PLONE_URL}
    Open Add New Menu
    Click Link  collection
    Input Text  form-widgets-IDublinCore-title  ${title}
    Select From List By Value  name=addindex  hiddenTags
    Click Button  Save
    Sleep  1
    Element Should Contain  css=.documentFirstHeading  ${title}


I set to the collection '${collection_title}' the search terms hidden tag '${keyword}'
    Go to  ${PLONE_URL}/${collection_title}
    Click Edit In Edit bar
    # Select From List By Value  name=addindex  hiddenTags
    Sleep  1
    Click Element  css=.querywidget.queryvalue.multipleSelectionWidget
    Select Checkbox  css=.querywidget.queryvalue.multipleSelectionWidget input[value=${keyword}]
    Click Button  Save


the collection '${collection_title}' should contain '${document_title}'
    Go to  ${PLONE_URL}/${collection_title}
    The content area should contain  ${document_title}


The content area should contain
    [Arguments]  ${text}
    Element Should Contain  id=content  ${text}
