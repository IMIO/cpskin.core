
# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s cpskin.core -t test_hidden_keyword.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path cpskin cpskin.core.testing.CPSKIN_CORE_ROBOT_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot cpskin/core/tests/robot/test_hidden_keyword.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings ***

Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Suite setup  Set Selenium speed  0.5s

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
    Click Link  Categorization
    Input Text  form.widgets.IHiddenTags.hiddenTags_additional  ${keyword}
    Click Button  Save
    Element Should Contain  id=hidden-tags  ${keyword}


a collection
    [Arguments]  ${title}
    ${folder_uid}  Create content  type=Folder  id=folder  title=folder
    Go to  ${PLONE_URL}/folder
    Open Add New Menu
    Click Link  collection
    Input Text  form-widgets-IDublinCore-title  ${title}
    # Select From List By Value  name=addindex  hiddenTags
    Click Button  Save
    Element Should Contain  css=.documentFirstHeading  ${title}


I set to the collection '${collection_title}' the search terms hidden tag '${keyword}'
    Go to  ${PLONE_URL}/folder/${collection_title}
    Click Edit In Edit bar
    Select From List By Value  name=addindex  hiddenTags
    # Click Element  css=.querywidget.queryvalue.multipleSelectionWidget
    Click Element  css=.querywidget.multipleSelectionWidget
    Select Checkbox  css=input[value=${keyword}]
    #Select Checkbox  css=.querywidget.queryvalue.multipleSelectionWidget input[value=${keyword}]
    Click Button  Save


the collection '${collection_title}' should contain '${document_title}'
    Go to  ${PLONE_URL}/folder/${collection_title}
    Element Should Contain  id=content  ${document_title}
