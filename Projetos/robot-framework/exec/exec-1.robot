*** Settings ***
Library        SeleniumLibrary

*** Variables ***
${url}    https://www.youtube.com/
${video}    class:yt-simple-endpoint 
${botaolike}    xpath:/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]


*** Keywords ***
Abrir site
    Open Browser     ${url}     chrome

Clicar no video
    Click Element     ${video}

Clicar no like
    Click Element     ${botaolike}
*** Test Cases ***
Cenário 1: Clicar em like no vídeo
    Abrir site
    Clicar no video
    Clicar no like
