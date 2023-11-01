*** Settings ***
Resource    bdd-resource.robot
Library    SeleniumLibrary
Resource    resources.robot

*** Test Cases ***
Caso de Teste 1: Cadastro sem nome
    Dado que estou na página de cadastro
    Quando preencho todos os campos do formulário de cadastro
    E não preencho o campo nome e envio o formulário
    Logo o sistema informa notificação de campos vazio
    Fechar navegador

Caso de Teste 2: Cadastro de usuário com nome composto
    Dado que estou na página de cadastro
    Quando preencho todos os campos de formulário de cadastro do nome composto
    E insiro o nome composto e clico em registrar
    Logo o sistema vai para outra página
    Fechar navegador

Caso de Teste 3: Cadastrar um usuário com um email que já foi cadastrado
    Dado que estou na página de cadastro
    Quando preencho todos os campos de formulário de cadastro (email)
    E preencho o campo email com um email já cadastrado e envio o formulário
    Logo o sistema informa que o email já está cadastrado
    Fechar navegador

Caso de Teste 4: Efetuar login do usuário com o campo email vazio 
    Dado que estou na página de login
    Quando preencho somente o campo senha
    E não preencho o campo de email
    Logo o sistema informa que o campo email não foi preenchido
    Fechar navegador

Caso de Teste 5: Efetuar do usuário com o campo senha inválido 
    Dado que estou na página de login
    Quando preencho o campo email
    E errei a senha
    Logo o sistema não efetua o login
    Fechar navegador
    
Caso de Teste 6: Cadastro de usuário com um apelido já cadastrado 
    Dado que estou na página de cadastro
    Quando preencho todos os campos de formulário de cadastro (apelido)
    E preencho campo apelido já cadastrado e clico em registrar
    Logo o sistema informa que o apelido já foi cadastrado
    Fechar navegador

Caso de Teste 7: Cadastro de usuário com todos os campos vazios 
    Dado que estou na página de cadastro
    Quando deixo todos os campos vazios
    E clico em registrar
    Logo o sistema informa que tem campos vazios
    Fechar navegador

Caso de Teste 19: Fazer o cadastro com o campo "Nome" com um número no final
    Dado que estou na página de cadastro
    Quando preencho todos os campos de formulário de cadastro (nome)
    E preencho o campo nome com um nome e um número e clico em registrar
    Logo o sistema informa que não pode ser cadastrado um nome com um número
    Fechar navegador

