lista = []
cont = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    cont += 1
    continuar = input("Quer continuar? [S/N]")
    if continuar in "Nn":
        break
print("-="*45)
print(f"Você digitou {cont} elementos!")
print("-="*45)
lista.sort(reverse=True)
print("A ordem decrescente dos números é {}".format(lista))
print("-="*45)
if 5 in lista:
    print("O valor 5 está na lista!")
else:
    print("O valor 5 não está na lista!")
print("-="*45)