import enum


lista = []
pares = list()
impares = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    continuar = input("Deseja continuar? [S/N] ")
    if continuar in "Nn":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f"A lista é {lista}")
print(f"Os números pares são: {pares}")
print(f"Os números impares são {impares}")