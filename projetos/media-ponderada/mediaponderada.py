# PROGRAMA QUE CALCULA A MÉDIA PONDERADA - ALUNO: DIOGO BONET SOBEZAK 
from multiprocessing.sharedctypes import Value
while True:
    try:
        quant = int(input("Digite quantas notas que você irá calcular a média?\n"))
        numnotas = 0
        numpesos = 0

        for i in range(1, quant + 1):
            notas = float(input("Digite o valor da {}ª nota:\n" .format(i)))
            pesos = int(input("Digite o valor {}° do peso:\n" .format(i)))
            numpesos = numpesos + pesos
            numnotas = numnotas + (notas * pesos)

        mediaponderada = numnotas / numpesos
        print("A média ponderada: {:.2f}" .format(mediaponderada))
        continuar = input("Você deseja continuar?\n")
        if continuar != "S":
            break
    except ValueError:
        print("Valor inválido! Tente novamente!")