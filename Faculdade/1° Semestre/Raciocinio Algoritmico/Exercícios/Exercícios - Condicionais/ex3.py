print("Par ou Ímpar")
num = int(input("Digite um número inteiro:\n"))
resul = num % 2

if resul == 0:
    print("O número {} é par!" .format(num))

if resul == 1:
    print("O número {} é ímpar!" .format(num))