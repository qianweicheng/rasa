*** Settings ***
Documentation    Suite description
...    line1
...    line2
Library    /Users/lidayuan/Documents/edison/nlu/rasa/edo_pro/robot/procedure.py


*** Variables ***
${a1}    a1
${a2}    a2
${a3}    a3
${a4}    a4


*** Test Cases ***
Test a1
    [Documentation]    this test is t1
    ${r1}    p1    ${a1}    ${a2}
    Run Keyword If    ${r1}    log to console    \n"ok"
    Log    a1 ok


Test a2
    ${r1}    p2    ${a1}    ${a2}
    Run Keyword If    ${r1}    log to console    \n"ok"
    ...    ELSE    log to console    \n"not ok"


Test train
    Import Library    /Users/lidayuan/Documents/edison/nlu/rasa/edo_pro/rasasc/rbout.py
    ${r1}    train


*** Keywords ***
Provided precondition
    Setup system under test