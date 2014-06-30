*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test cases ***

Scenario: Test collection hidden tags criteria
    Given logged as owner
      And a document 'simple_document' with hidden tag 'sample_keyword'
      And a collection  simple_collection
     When I set to the collection 'simple_collection' the search terms hidden tag 'sample_keyword'
     Then the collection 'simple_collection' should contain 'simple_document'


*** Keywords ***

logged as owner
    Log in as site owner


a document '${title}' with hidden tag '${keyword}'
    Go to  ${PLONE_URL}
    Add document  ${title}
    Click Edit In Edit bar
    Click Link  Categorization
    Input Text  hiddenTags_keywords  ${keyword}
    Click Button  Save
    Element Should Contain  id=hidden-tags  ${keyword}


a collection
    [Arguments]  ${title}
    Go to  ${PLONE_URL}
    Add content  collection  ${title}


I set to the collection '${collection_title}' the search terms hidden tag '${keyword}'
    Go to  ${PLONE_URL}/${collection_title}
    Click Edit In Edit bar
    Select From List By Value  name=addindex  HiddenTags
    Select Checkbox  css=.querywidget.queryvalue.multipleSelectionWidget input[value=${keyword}]
    Click Button  Save


the collection '${collection_title}' should contain '${document_title}'
    Go to  ${PLONE_URL}/${collection_title}
    The content area should contain  ${document_title}


The content area should contain
    [Arguments]  ${text}
    Element Should Contain  id=content  ${text}
