cont = 0
numero = 0
while True:
    num = int(input("Digite um número: "))
    continuar = input("Deseja continuar [S/N]: ").upper()
    cont += 1
    if continuar == "n" or continuar == "N":
        break
    

print(f"Você digitou {cont}")
