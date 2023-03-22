import json


#Matriz principal que será salva.
matrizMaior = []


#Def ler json.
def loadDb(variavel):
    with open('Matriz.json', 'r') as rMatriz:
        variavel = json.load(rMatriz)
    return variavel


#Leitura da matriz salva.
matrizMaior = loadDb(matrizMaior)


#Def salvar em json.
def saveDb(data):
    with open('Matriz.json', 'w') as wMatriz:
        json.dump(data, wMatriz)


#Def topo do menu principal. (Estética)
def menuMatrizTopo():
    print("="*55)
    print("                    MenuMatrizes")
    print("="*55)


#Def menu de escolhas do menu de matrizes.
def menuMatrizPrincipal():
    print("\n\033[0;33m[ 1 ] | Criar Matriz")
    print("[ 2 ] | Determinante 2x2")
    print("[ 3 ] | Determinante 3x3")
    print("[ 4 ] | Transposta")
    print("\033[31m[ 5 ] | Sair")

    while True:
        op = input("\033[0;0m-> ")
       
        if op == "1":
            criarMatriz()
            break
        if op == "2":
            det2x2()
            break
        if op == "3":
            det3x3()
            break
        if op == "4":
            matrizTransposta()
            break
        if op == "5":
            print("\033[0;91mSaindo...\033[0;0m")
            break
        else:
            pass
            print("\n\033[0;91mValor Inválido! Tente novamente!")
            menuMatrizPrincipal()


#Def de mostrar matriz como matriz, e não lista.
def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print('\n')


#Def de criar a matriz de qualquer tamanho.
def criarMatriz():
    if matrizMaior != []:
        opdel = input('Deseja continuar? a matriz existente será deletada!\n(S) para continuar: ')
        if opdel == 'S' or opdel == 's':
            matrizMaior.clear()
            print('\n \033[0;32mMatriz Excluida com sucesso!\u001b[0m \n')
            saveDb(matrizMaior)
        else:
            menuMatrizPrincipal()
    matriz_linhas = int(input('Quantidade de linhas: '))
    matriz_colunas = int(input('Quantidade de colunas: '))
    matcontrol = 0


    for quantLinhas in range(0, matriz_linhas):
        matrizMaior.append(0)
        matrizMenor = []
        for c in range(0, matriz_colunas):
            matrizMenor.append(0)
        matrizMaior[matcontrol] = matrizMenor
        matcontrol += 1


    mostrarMatriz(matrizMaior)


    for linha in range(0, matriz_linhas):
        for coluna in range(0, matriz_colunas):
            print(f'Linha[{linha}] Coluna[{coluna}]:')
            matrizMaior[linha][coluna] = float(input(f'Digite valor para {linha, coluna}: '))
            mostrarMatriz(matrizMaior)
    saveDb(matrizMaior)
    from main import menuPrincipal
    menuPrincipal()


#Def de determinante de uma matriz 2x2.
def det2x2():
#Verificador se é uma matriz 2x2.
    verify2L = 0
    verify2C = 0
    for l in range(0, len(matrizMaior)):
        verify2L += 1
        for c in matrizMaior[l]:
            verify2C += 1
    if verify2L == 2 and verify2C == 4:
#Achando o determinante da Matriz caso ela seja 2x2.
        determinante2x2 = (matrizMaior[0][0] * matrizMaior[1][1]) - (matrizMaior[0][1] * matrizMaior[1][0])
        print(f'\033[0;32mdet(2x2) = {determinante2x2}\u001b[0m')
        input('[ENTER] para continuar...')
        print('\n')
        from main import menuPrincipal
        menuPrincipal()
    else:
        print('Não é possível fazer determinante com essa matriz!')


def det3x3():
#Verificador se é uma matriz 3x3.
    verify3L = 0
    verify3C = 0
    for l in range(0, len(matrizMaior)):
        verify3L += 1
        for c in matrizMaior[l]:
            verify3C += 1
    if verify3L == 3 and verify3C == 9:
        determinante3x3L1 = (matrizMaior[0][0] * matrizMaior[1][1] * matrizMaior[2][2])+(matrizMaior[0][1] * matrizMaior[1][2] * matrizMaior[2][0])+(matrizMaior[0][2] * matrizMaior[1][0] * matrizMaior[2][1])
        determinante3x3L2 = (matrizMaior[0][2] * matrizMaior[1][1] * matrizMaior[2][0])+(matrizMaior[0][0] * matrizMaior[1][2] * matrizMaior[2][1])+(matrizMaior[0][1] * matrizMaior[1][0] * matrizMaior[2][2])
        determinante3x3 = (determinante3x3L1 - determinante3x3L2)
        print(f'\033[0;32mdet(3x3) = {determinante3x3}\u001b[0m')
        input('[ENTER] para continuar...')
        print('\n')
        from main import menuPrincipal
        menuPrincipal()
    else:
        print('Não é possível fazer determinante com essa matriz!')
#Achando o determinante da Matriz caso ela seja 3x3.

#Def de Matriz transposta.
def matrizTransposta():
    matrizMaiorTransposta = []


    novaQuantColunas = len(matrizMaior)
    novaQuantLinhas = len(matrizMaior[0])

    matriz_linhas = novaQuantLinhas
    matriz_colunas = novaQuantColunas
    matcontrol = 0


    for quantLinhas in range(0, matriz_linhas):
        matrizMaiorTransposta.append(0)
        matrizMenor = []
        for c in range(0, matriz_colunas):
            matrizMenor.append(0)
        matrizMaiorTransposta[matcontrol] = matrizMenor
        matcontrol += 1


    mostrarMatriz(matrizMaior)


    for l in range(0, novaQuantLinhas):
        for c in range(0, novaQuantColunas):
            matrizMaiorTransposta[l][c] = matrizMaior[c][l]
    

    mostrarMatriz(matrizMaiorTransposta)
    
    input('[ENTER] para continuar...')
    print('\n')
    from main import menuPrincipal
    menuPrincipal()


            