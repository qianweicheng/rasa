*** Test Cases ***
First Case
    Log    Hello World!    warn

Second Case
    ${res}    Evaluate    1+2+3
    Should Be Equal    ${res}    6

Third Case
    ${res}    Evaluate    'i'*3
    Length Should Be    ${res}
