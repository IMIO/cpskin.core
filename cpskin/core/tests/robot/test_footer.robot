*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Variables ***


*** Test cases ***


Test static footer visible
    Page Should Contain Link   LOISIRS
    Click Link                 LOISIRS
    Element Should Be Visible  css=ul.navTreeLevel0 a#loisirs-art_et_culture
    Click Element              css=ul.navTreeLevel0 a#loisirs-art_et_culture
    Element Should Be Visible  css=ul.navTreeLevel1 a#loisirs-art_et_culture-artistes
    Click Element              css=ul.navTreeLevel1 a#loisirs-art_et_culture-artistes
    Element Should Be Visible  css=ul.navTreeLevel2 a#loisirs-art_et_culture-artistes-tata
    Click Element              css=ul.navTreeLevel2 a#loisirs-art_et_culture-artistes-tata

    Location Should Be  http://localhost:55001/plone/loisirs/art_et_culture/artistes/tata

Test edit static footer
    Page Should Contain Link  LOISIRS

    Click Link          LOISIRS
    Location Should Be  http://localhost:55001/plone/loisirs
    Click Element       css=ul.navTreeLevel0 a#loisirs-art_et_culture
    Location Should Be  http://localhost:55001/plone/loisirs
    Click Element       css=ul.navTreeLevel1 a#loisirs-art_et_culture-bibliotheques
    Location Should Be  http://localhost:55001/plone/loisirs/art_et_culture/bibliotheques
