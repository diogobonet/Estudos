*** Settings ***
Resource    bdd-resource.robot
Library    SeleniumLibrary

*** Variables ***
${Browser}  chrome
${URL-register}  http://localhost/Got-an-Idea/register/registro.php
${URL-login}  http://localhost/Got-an-Idea/login/login.php
${input_nome}    name:nome_input
${input_sobrenome}  name:sobrenome_input
${input_email}  name:email_input
${input_apelido}  name:apelido_input
${input_senha}    name:senha_input
${input_confirmar}    name:confirmar_input
${input_senha_login}  id:password
${submit}    id:botao_submit
${button_join}    xpath:/html/body/main/div/div/div[2]/div/form/button
${input_email_login}  id:email
${notificacao_div}        id:notificacao_div
${campo-vazio}    ${None}

*** Keywords ***
# Dado que:
estou na página de cadastro
    Open Browser    ${URL-register}   ${browser}
    Maximize Browser Window

estou na página de login
    Open Browser     ${URL-login}    ${browser}
    Maximize Browser Window

# Caso de Teste 1: Cadastro sem nome
preencho todos os campos do formulário de cadastro
    Input Text    ${input_sobrenome}    Souza
    Sleep    1s
    Input Text    ${input_email}    fernando_luiz_dapaz@patriciagrillo.adv.br
    Sleep    1s
    Input Text    ${input_apelido}    fernandoluiz
    Sleep    1s
    Input Password    ${input_senha}    D@123456
    Sleep    1s
    Input Password    ${input_confirmar}    D@123456
    Sleep    1s

não preencho o campo nome e envio o formulário
    Click Element    ${submit}
    Sleep     8s
    
o sistema informa notificação de campos vazio
    Page Should Contain    Um dos campos está vazio... Por favor preencha-o!

# Caso de Teste 2: Cadastro de usuário com nome composto
preencho todos os campos de formulário de cadastro do nome composto
    Input Text    ${input_sobrenome}    Fernandes
    Sleep    1s
    Input Text    ${input_email}    anadepaula@email.com
    Sleep    1s
    Input Text    ${input_apelido}    anadepaula
    Sleep    1s
    Input Password    ${input_senha}    D@123456
    Sleep    1s
    Input Password    ${input_confirmar}    D@123456
    Sleep    1s

insiro o nome composto e clico em registrar
    Input Text    ${input_nome}    Ana de Paula
    Sleep    1s
    Click Element    ${submit}
    Sleep     8s

o sistema vai para outra página
    Page Should Contain    Qual é o seu propósito?

# Caso de Teste 3: Cadastrar um usuário com um email que já foi cadastrado
preencho todos os campos de formulário de cadastro (email)
    Input Text    ${input_nome}    Teste 
    Sleep    1s
    Input Text    ${input_sobrenome}    Email
    Sleep    1s
    Input Text    ${input_apelido}    testeemail
    Sleep    1s
    Input Password    ${input_senha}    D@123456
    Sleep    1s
    Input Password    ${input_confirmar}    D@123456
    Sleep    1s

preencho o campo email com um email já cadastrado e envio o formulário
    Input Text    ${input_email}    anadepaula@email.com   # Já foi cadastrado no CT02
    Sleep    1s
    Click Element    ${submit}
    Sleep     8s

o sistema informa que o email já está cadastrado
    Page Should Contain    Email já cadastrado... Por favor tente novamente!

# Caso de Teste 4: Efetuar login do usuário com o campo email vazio 
preencho somente o campo senha
    Input Text    ${input_senha_login}  D@123456
    Sleep    3s

não preencho o campo de email
    Click Element  ${button_join}
    Sleep     8s

o sistema informa que o campo email não foi preenchido
    Wait Until Page Does Not Contain    Você tem uma ideia?

# Caso de Teste 5: Cadastro de usuário sem nome
preencho o campo email
    Input Text    ${input_email_login}   ana@email.com
    Sleep    2s

errei a senha
    Input Text    ${input_senha_login}    eeeee
    Sleep    2s
    Click Element  ${button_join}
    Sleep     8s

o sistema não efetua o login
    Page Should Contain    Email ou senha incorretos... Por favor tente novamente

# Caso de Teste 6: Cadastro de usuário com um apelido já cadastrado 
preencho todos os campos de formulário de cadastro (apelido)
    Input Text    ${input_nome}    Teste
    Sleep    1s
    Input Text    ${input_sobrenome}    Apelido
    Sleep    1s
    Input Text    ${input_email}    testeemail@email.com
    Sleep    1s
    Input Password    ${input_senha}    D@123456
    Sleep    1s
    Input Password    ${input_confirmar}    D@123456
    Sleep    1s

preencho campo apelido já cadastrado e clico em registrar
    Input Text    ${input_apelido}    anadepaula   # Já foi cadastrado no CT02
    Sleep    1s
    Click Element    ${submit}
    Sleep     8s

o sistema informa que o apelido já foi cadastrado
    Page Should Contain    Apelido já utilizado... Por favor tente novamente!

# Caso de Teste 7: Cadastro de usuário com todos os campos vazios 
clico em registrar
    Click Element    ${submit}
    Sleep     8s

deixo todos os campos vazios
    Clear Element Text    ${input_nome}
    
o sistema informa que tem campos vazios
    Page Should Contain    Um dos campos está vazio... Por favor preencha-o!

# Caso de Teste 19: Fazer o cadastro com o campo "Nome" com um número no final
preencho todos os campos de formulário de cadastro (nome)
    Input Text    ${input_sobrenome}    Nomenum
    Sleep    1s
    Input Text    ${input_email}    nomenum@email.com
    Sleep    1s
    Input Text    ${input_apelido}    nomenum   # Já foi cadastrado no CT02
    Sleep    1s
    Input Password    ${input_senha}    D@123456
    Sleep    1s
    Input Password    ${input_confirmar}    D@123456
    Sleep    1s

preencho o campo nome com um nome e um número e clico em registrar
    Input Text    ${input_nome}    Diogo2
    Sleep    1s
    Click Element    ${submit}
    Sleep     8s

o sistema informa que não pode ser cadastrado um nome com um número
    Wait Until Element Is Visible      ${notificacao_div} 
    Page Should Contain    Nome: entre 2&25 caracteres e começar com maiúscula

Fechar navegador
    Close Browser
