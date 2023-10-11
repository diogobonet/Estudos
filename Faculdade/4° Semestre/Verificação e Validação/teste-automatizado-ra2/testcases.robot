*** Settings ***
Resource  ./index.robot

*** Test Cases ***
CT01 - Cadastro de usuário sem nome
    Abrir a página de cadastro de usuário
    Preencher todos os campos menos o campo nome
    Clicar em Registrar
    Verificar campos vazios 
    Fechar navegador

CT02 - Cadastro de usuário com nome composto
    Abrir a página de cadastro de usuário
    Cadastro de usuário com nome composto
    Clicar em Registrar
    Fechar navegador

CT03 - Cadastrar um usuário com um email que já foi cadastrado
    Abrir a página de cadastro de usuário
    Cadastrar um usuário com um email que já foi cadastrado
    Clicar em Registrar
    Verificar notificação de email cadastrado
    Fechar navegador

CT04 - Efetuar login do usuário com o campo email vazio
    Abrir a página de login
    Preencher o campo senha
    Clicar em Entrar
    Verificar email não preenchido
    Fechar navegador

CT05 - Efetuar do usuário com o campo senha inválido
    Abrir a página de login
    Preencher o campo email
    Preencher o campo senha com a credencial errada
    Clicar em Entrar
    Verificar mensagem de senha incorreta
    Fechar navegador

CT06 - Cadastro de usuário com um apelido já cadastrado 
    Abrir a página de cadastro de usuário
    Cadastro de usuário com um apelido já cadastrado 
    Clicar em Registrar
    Verificar notificação de apelido cadastrado
    Fechar navegador

CT07 - Cadastro de usuário com todos os campos vazios 
    Abrir a página de cadastro de usuário
    Clicar em Registrar
    Verificar campos vazios
    Fechar navegador

CT19 - Fazer o cadastro com o campo "Nome" com um número no final
    Abrir a página de cadastro de usuário
    Cadastro de usuário com nome possuindo número
    Clicar em Registrar
    Verificar mensagem de número não permitido
    Fechar navegador