*** Settings ***
Library        SeleniumLibrary

*** Variables ***
${URL}  https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit
${Browser}    chrome
${input_name}    name:fname
${input_lastname}    name:lname
${submit}    value:submit


*** Keywords ***
Abrir site
    Open Browser  ${URL}  ${Browser}

Preencher dados
    Input Text    ${input_name}  Diogo
    Input Text    ${input_lastname}  Sobezak


Enviar formulário
    Click Element    ${submit}

*** Test Cases ***
TC01 - Preencher formulário
    Abrir site
    Preencher dados
    Enviar formulário