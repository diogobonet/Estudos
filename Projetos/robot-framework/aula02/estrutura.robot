*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${variavel1}    teste
${variavel2}    hhhh
${variavel3}    www.amazon.com

*** Keywords* **
Abrir site da amazon  
    Open Browser    https://www.amazon.com.br/
Fechar navegador
    Close Browser
Abrir site da netflix  
    Open Browser    https://www.netflix.com/br/

*** Test Cases ***
Cenário 1: Teste de abrir o site da Amazon
    Abrir site da amazon 
    Fechar navegador 

Cenário 2: Teste abrir site netflix
    Abrir site da netflix 
    Fechar navegador  
    

