num = cont = soma  = 0
while num != 999:
        num = int(input("Digite um número [999 para parar]: "))
        cont += 1
        soma += num
print("Você digitou {} números. A soma desses números é: {}".format(cont - 1, soma - 999))