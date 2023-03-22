print("Calcúlo de Bhaskara")
valueA = int(input("Digite o valor de A:\n"))
valueB = int(input("Digite o valor de B:\n"))
valueC = int(input("Digite o valor de C:\n"))

# CALCULO DO 
delta = (valueB ** 2) - 4 * valueA * valueC

print("O valor de delta é '{}'" .format(delta))

if delta == 0 or delta < 0:
    x = -valueB / (2 * valueA)
    print("O delta é negativo, portanto não existe raiz. O valor é: ", x)

if delta > 0:
    x1 = (-valueB + delta ** (1/2) / (2 * valueA))
    x2 = (-valueB - delta ** (1/2) / (2 * valueA))
    print("O valor de x1 é {:.2f}" .format(x1))
    print("O valor de x2 é {:.2f}" .format(x2))
else:
    print("Você digitou um valor inválido! Tente novamente!")