C = int(input("Digite o capital aplicado: "))
i = int(input("Digite a taxa de juros em %: "))
n = int(input("Digite o tempo da aplicação em (meses): "))
i = i / 100
M = C * ((1+ i) ** n)
print("O montante final dos juros é R${:.2f}" .format(M))