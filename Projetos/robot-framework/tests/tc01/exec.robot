*** Settings ***
Library        SeleniumLibrary
Resource    ../../aula03/form.robot

*** Variables ***
${Browser}     chrome
${URL}    https://robotframework.org/
${docs}    xpath://*[@id="app"]/div[3]/div/div[2]/div/button
${guides}    xpath://*[@id="app"]/div[3]/div/div[2]/div/div/div[1]/a
${rpa}    xpath://*[@id="docusaurus_skipToContent_fallback"]/div/main/div/div/div/div/article/div/div[1]/div/a[2]/div[2]/div[1]
${rpatext}    RPA

*** Keywords ***
[Keywords]   Abrir navegador
    Open Browser    ${URL}    ${Browser}
Abrir navegador no site do Robotframework
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window

Clicar em docs
    Click Element    ${docs}
    Wait Until Element Is Visible    ${guides}
    Click Element    ${guides}

*** Test Cases ***
TC01 - Abrir site
    Abrir navegador
    Clicar em docs
