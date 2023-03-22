# I M P O R T S
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import verifycpf
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def verifyAge(idade):
    while True:
        if idade < 18 or idade > 122:
            print(f'\n[{idade}] é inválido, apenas maiores de 18 e menores que 122')
            idade = int(input('Idade: '))
        if idade >= 18 and idade <= 122:
            return idade
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def verifyCpf(cpf):
    pass
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def verifyName(name):
    letras = 'abcdefghijklmnopqrstuvwxyzãáéíóúçABCDEFGHIJKLMNOPQRSTUVWXYZÃÁÉÍÓÚÇ '
    for l in name:
        if l in letras:
            print(f'Tem {l}')
        else:
            print(f'[{l}] é uma letra inválida!')
            name = input('Nome: ')
            return verifyName(name)
    return name
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def cad():
    name = input('• Nome: ')
    name = verifyName(name)
    idade = int(input('• Idade: '))
    idade = verifyAge(idade)
    cpf = input('• Cpf:')
    while True:
        cpfSave = cpf
        cpf = verifycpf.cpf_valido(cpf)
        if cpf == True:
            cpf = cpfSave
            break
        else:
            print('CPF Inválido!')
            cpf = input('• Cpf:')
    cdoc = {'nome': name, 'idade': idade, 'cpf': cpf}
    print("Cadastro concluido!")
    return cdoc
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def sair():
    print("Cadastro concluido!")
