*** Settings ***
Library    Collections

*** Variables ***
${NAME}    Robot Framework

*** Test Cases ***
Simple Test
    Log    Hello, ${NAME}
    Should Be Equal    ${NAME}    Robot Framework

List Test
    @{items}=    Create List    apple    banana    orange
    Length Should Be    ${items}    4    msg=Items length is not equal to 4