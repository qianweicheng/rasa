*** Settings ***
Documentation    Suite description
...    line1
...    line2

*** Variables ***

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Provided precondition
    When action
    Then check expectations

*** Keywords ***
Provided precondition
    Setup system under test