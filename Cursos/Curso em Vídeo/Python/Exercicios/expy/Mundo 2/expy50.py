soma = 0
cont = 0
for c in range(6):
    num = int(input("Digite o {}° número: ".format(str(c+1))))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print("Você informou {} números pares, portanto sua soma é igual a {}!".format(cont, soma))