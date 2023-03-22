c = float(input("Insira o valor inicial a ser aplicado: "))
juros = float(input("Insira a taxa de juros mensal: "))
juros = juros / 100
n = int(input("Insira o tempo da aplicação em meses: "))

valorFinal = c

for i in range(n):
  valorFinal += juros * valorFinal

print('Seu saldo final será de: {:.2f}'.format(valorFinal))
