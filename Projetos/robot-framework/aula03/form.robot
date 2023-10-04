*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${input_name}    id:fname
${input_lastname}   id:lname
${input_email}      id:email
${input_password}   id:password
${input_confirmpassword}    id:confirmPassword
${button_submit}    id:sub

*** Keywords ***
Abrir navegador
    Open Browser    https://app.formtester365.com/signup    chrome

Preencher campos
    Input Text  ${input_name}    Robson
    Input Text  ${input_lastname}    Zimmerman
    Input Text  ${input_email}   robson@email.com
    Input Text  ${input_password}    123456
    Input Text  ${input_confirmpassword}     123456
     
Enviar formulario
    Click Element    ${button_submit}

Fechar navegador
    Close Browser

*** Test Cases ***
Cenário 1: Preencher formulário
    Abrir navegador
    Preencher campos
    Enviar formulario
    Fechar navegador