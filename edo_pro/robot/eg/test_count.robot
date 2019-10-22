*** Test Cases ***

test case12
    Import Library    /Users/lidayuan/Documents/RPA/robotframework/example/count.py
    ${a}    Evaluate    int(4)
    ${b}    Evaluate    int(5)
    ${add}    add    ${a}    ${b}
    log    ${add}