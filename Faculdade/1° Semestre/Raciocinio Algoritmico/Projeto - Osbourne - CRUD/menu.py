#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Funções feitas em outros arquivos:
import cadastroprodutos
import clientes
#OBS: Elas só funcionam juntas!
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Função do menu inicial:
def menu():
    print('='*55)
    print('               [Nós somos do rock]\n')
    print('Gabriel Mocellin; Diogo Bonet; Eduardo Mussi; André Akim')
    print('PUCPR BES 2022-1')
    print('='*55)
    print('\n\n[1] Cadastro de Cliente')
    print('[2] Cadastro de Jogo')
    print('[3] Compra de Jogo')
    print('[4] Cadastro de (x)')
    while True:
        op = input('-> ')
        if op == '1':
            print('\n\n')
            print(clientes.cad())
        if op == '2':
            print('\n\n')
            print(cadastroprodutos.menuprod())
            break
        if op == '3':
            break
        if op == '4':
            break
        else:
            print('\033[31mValor inválido!\033[0;0m')
            menu()
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

menu()