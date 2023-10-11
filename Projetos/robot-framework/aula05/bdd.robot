*** Settings ***
Library        SeleniumLibrary

*** Variables ***
# DADOS
${NomeDaMusica}    Toto - Africa

# VARIAVEIS DE CONFIGURAÇÃO
${URL}        https://www.youtube.com
${Browser}        chrome     

# ELEMENTOS DE PESQUISA
${Input_Pesquisa}    id:search
${Botao_Submit}    xpath://*[@id="search-icon-legacy"]
${Video}    xpath://yt-formatted-string[@class="style-scope ytd-video-render"][1]
${Prova}    xpath://yt-formatted-string[contains(text(), "Compartilhar")]  # Correção aqui

*** Keywords ***
Dado que eu acesso o site do youtube
    Open Browser    ${URL}    ${Browser}

Quando digito o nome da música
    Element Should Be Enabled     id:search
    Input Text    ${Input_Pesquisa}  ${NomeDaMusica}

E clico no botão buscar
    Click Element    ${Botao_Submit}

E clico na primeira opção da lista
    Wait Until Element Is Visible    ${Video}    10
    Click Element    ${Video}

Então o vídeo é executado
    Wait Until Element Is Visible    ${Prova}    10
    Element Should Be Visible    ${Prova}
    Sleep    1s
    Close Browser

*** Test Cases ***
Cenario 1: Executar vídeo no site do youtube
    Dado que eu acesso o site do youtube
    Quando digito o nome da música
    E clico no botão buscar
    E clico na primeira opção da lista
    Então o vídeo é executado
