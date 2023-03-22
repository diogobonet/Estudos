lista = []
while True:
    num = input("Digite um número: ")
    continuee = input("Deseja continuar? [s/n]")
    lista.append(num)
    if continuee != "s":
        break
print(f"Os números que você digitou foi: {lista}")