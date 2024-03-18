'''c = 1 
while c < 10:
    print(c)
    c += 1
print("FIM")'''

 # O WHILE SERVE PARA QUANDO VOCÊ SABE OU NÃO UM LIMITE DE UMA AÇÃO

'''r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("FIM!")'''

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if  n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} números ímpares!".format(par, impar))