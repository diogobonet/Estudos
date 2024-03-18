soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma = soma + c
print("Os {} valores solicitados somados dão no total {}".format(cont, soma))