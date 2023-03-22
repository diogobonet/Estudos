# Calculadora de Funções e Matrizes  - Alunos Diogo Sobezak, Eduardo Mussi e Gabriel Mocellin
# import numpy as np
# import matplotlib.pyplot as plt
import time

# Menu Principal
print("\033[0;97m="*55)
print("\033[0;94m                    Calculadora")
print("\033[0;97m="*55)

def menuPrincipal():
    print("\n\033[0;33m[ 1 ] | Função de Segundo Grau")
    print("[ 2 ] | Funções Exponenciais")
    print("[ 3 ] | Matrizes")
    print("\033[31m[ 4 ] | Sair")
    while True:
        op = input("\033[0;0m-> ")
       
        if op == "1":
            funcaosegundograu()
        if op == "2":
            funcaoexponencial()
        if op == "3":
            print("3")
            menuPrincipal()
        if op == "4":
            print("\033[0;91mSaindo...\033[0;0m")
            break
        else:
            pass
            

def funcaosegundograu():
    print("="*55)
    print("                   Função Segundo Grau")
    print("="*55)
    valueA = float(input("Valor A: "))
    valueB = float(input("Valor B: "))
    valueC = float(input("Valor C: "))
    print("\n\033[0;33m[ 1 ] | Calcular raizes")
    print("[ 2 ] | Calcular função em x pedido")
    print("[ 3 ] | Calcular vértice")
    print("[ 4 ] | Gerar gráfico")
    print("\033[31m[ 5 ] | Voltar para o Menu Principal\033[0;0m")
    op = input("\n-> ")
    if op == "1":
        delta = (valueB**2) - (4 * valueA * valueC)
    # Raizes
        x1 = (-valueB+ delta**(1.0/2.0)) / (2.0*valueA)
        x2 = (-valueB- delta**(1.0/2.0)) / (2.0*valueA)
        print(f"O delta é: {delta}")
        print("Calculando...")
        time.sleep(0.6)
        print("x1: {:.2f}".format(x1))
        print("x2: {:.2f}".format(x2))
    if op == "2":
        pass
    if op == "3":
        pass
    if op == "4":
        pass 
    if op == "5":
        print("\033[31mVoltando para o menu...\033[0;0m")
        menuPrincipal()

def funcaoexponencial():
    print("\033[0;97m="*55)
    print("\033[0;94m                  Função Exponencial")
    print("\033[0;97m="*55)
    try:
        valueA = float(input("Valor A: "))
        valueB = float(input("Valor B: "))
    except:
        print("\033[31mOs valores A e B deveram ser apenas números!\033[0;0m")
        return funcaoexponencial()            
    print("\n\033[0;33m[ 1 ] | Verificar (Crescente ou Decrescente)")
    print("[ 2 ] | Calcular função em x pedido")
    print("[ 3 ] | Gerar gráfico")
    print("\033[31m[ 4 ] | Voltar para o menu\033[0;0m")
    if valueA == 0 or valueB == 0:
        print("\033[31mO valor não pode ser igual a 0!\033[0;0m")
        return funcaoexponencial()
    try:
        while True:
            op = input("\n\033[0;0m-> ")
            if op == "1":
                if valueA >= 1:
                    print("\033[0;32mCrescente!\033[0;0m")
                if valueA <= 0 or valueA <= 1:
                    print("\033[0;91mDecrescente!\033[0;0m")
                    funcaoexponencial()
            elif op == "2":
                valorX = float(input("Valor de X: "))
                if valorX == 0:
                    print("Valor inválido! Tente novamente!")
                    funcaoexponencial()
                else:    
                    y = valueA * valueB ** valorX 
                    print(f"f({valorX}) = {y}")
                    return 
            elif op == "3":
                # x = [valueA]
                # y = [valueB]
                # w = np.exp(valueA)
                # z = np.exp(valueB)
                # plt.figure()
                # plt.plot([w, z])
                # plt.show()
                funcaoexponencial()
            elif op == "4":
                menuPrincipal()
            else:
                print("\033[31mTente novamente!\033[0;0m")
    except ValueError: 
        print("\033[31mTente novamente!\033[0;0m")
# Rodar o code
menuPrincipal()
