def todos_numeros_iguais(cpf):
    i = 0 
    while i < len(cpf):
        if cpf[i-1] != cpf[i]:
            return False
        i += 1
    return True

def recupera_soma(cpf, fator):
    resultado = 0 
    for n in cpf[:9]:
        resultado += int(n) * fator
        fator -= 1
    return resultado

def recupera_primeiro_digito(cpf):

    soma = recupera_soma(cpf, 10)
    resultado = (soma * 10) % 11 
    if resultado == 10:
        return 0 
    return resultado

def recupera_segundo_digito(cpf, primeiro_digito):
    soma = recupera_soma(cpf, 11)
    soma += (primeiro_digito * 2)
    resultado = (soma * 10) % 11 
    if resultado == 10:
        return 0 
    return resultado 

def cpf_valido(cpf):
    if len(cpf) != 11 or not cpf.isnumeric() or todos_numeros_iguais(cpf):
        return False
    digito1 = recupera_primeiro_digito(cpf)
    digito2 = recupera_segundo_digito(cpf, digito1)
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

if __name__ == '__main__':
    print('Informe o seu CPF: ')
    cpf = input()
    if cpf_valido(cpf):
        print('CPF é válido')
    else:
        print('CPF inválido')