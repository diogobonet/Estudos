*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Dado que ${keyword}
    Run Keyword    ${keyword}

Quando ${keyword}
    Run Keyword    ${keyword}

E ${keyword}
    Run Keyword    ${keyword}

Logo ${keyword}
    Run Keyword    ${keyword}