*** Settings ***
Library  SeleniumLibrary

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

*** Keywords ***
Abrir a página de cadastro de usuário
    Open Browser    ${URL-register}  ${Browser}
    Maximize Browser Window

Abrir a página de login
    Open Browser    ${URL-login}  ${Browser}
    Maximize Browser Window

Preencher todos os campos menos o campo nome
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

Cadastro de usuário com nome composto
    Input Text    ${input_nome}    Ana de Paula
    Sleep    1s
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

Cadastrar um usuário com um email que já foi cadastrado
    Input Text    ${input_nome}    Teste 
    Sleep    1s
    Input Text    ${input_sobrenome}    Email
    Sleep    1s
    Input Text    ${input_email}    anadepaula@email.com   # Já foi cadastrado no CT02
    Sleep    1s
    Input Text    ${input_apelido}    testeemail
    Sleep    1s
    Input Password    ${input_senha}    D@123456
    Sleep    1s
    Input Password    ${input_confirmar}    D@123456
    Sleep    1s


Cadastro de usuário com um apelido já cadastrado 
    Input Text    ${input_nome}    Teste
    Sleep    1s
    Input Text    ${input_sobrenome}    Apelido
    Sleep    1s
    Input Text    ${input_email}    testeemail@email.com
    Sleep    1s
    Input Text    ${input_apelido}    anadepaula   # Já foi cadastrado no CT02
    Sleep    1s
    Input Password    ${input_senha}    D@123456
    Sleep    1s
    Input Password    ${input_confirmar}    D@123456
    Sleep    1s

Preencher o campo senha
    Input Text    ${input_senha_login}  D@123456
    Sleep    3s

Preencher o campo email
    Input Text    ${input_email_login}  anadepaula@email.com 
    Sleep    2s

Preencher o campo senha com a credencial errada
    Input Text    ${input_senha_login}  123456
    Sleep    3s

Verificar notificação de apelido cadastrado
    Page Should Contain    Apelido já utilizado... Por favor tente novamente!

Verificar notificação de email cadastrado
    Page Should Contain    Email já cadastrado... Por favor tente novamente!

Verificar campos vazios 
   Page Should Contain    Um dos campos está vazio... Por favor preencha-o!

Verificar email não preenchido
    Wait Until Page Does Not Contain    Você tem uma ideia?

Verificar mensagem de senha incorreta
    Page Should Contain    Email ou senha incorretos... Por favor tente novamente

Verificar mensagem de número não permitido
    Wait Until Element Is Visible      ${notificacao_div} 
    Page Should Contain    Nome: entre 2&25 caracteres e começar com maiúscula

Cadastro de usuário com nome possuindo número
    Input Text    ${input_nome}    Ana2
    Sleep    1s
    Input Text    ${input_sobrenome}    Fernandes
    Sleep    1s
    Input Text    ${input_email}    testenum@email.com
    Sleep    1s
    Input Text    ${input_apelido}    testenum
    Sleep    1s
    Input Password    ${input_senha}    D@123456
    Sleep    1s
    Input Password    ${input_confirmar}    D@123456
    Sleep    1s

Clicar em Registrar
    Click Element    ${submit}
    Sleep     8s

Clicar em Entrar
    Click Element  ${button_join}
    Sleep     8s

Fechar navegador
    Close Browser