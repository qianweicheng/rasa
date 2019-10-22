*** Test Cases ***

test case12
    Import Library    /Users/lidayuan/Documents/edison/nlu/rasa/edo_pro/robot/eg/count.py
    ${a}    Evaluate    int(4)
    ${b}    Evaluate    int(5)
    ${add}    add    ${a}    ${b}
    log    ${add}