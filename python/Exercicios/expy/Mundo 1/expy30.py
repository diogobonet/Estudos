print("JOGO DE PAR OU IMPAR")
n1 = int(input("Digite um número: "))
resultado = n1 % 2
if resultado == 0:
    print("O número {} é par!" .format(n1))
else:
    print("O número {} é impar!" .format(n1))
