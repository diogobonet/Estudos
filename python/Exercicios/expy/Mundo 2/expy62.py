print("Gerador de PA")
print("-="*15)
primeirotermo = int(input("Primeiro termo:"))
razãodopa = int(input("Razão do PA: "))
cont = 1
total = 0
termo = primeirotermo
add = 10
while add != 0:
    while cont <= total:
        total = total + add
        print("{} -> ".format(termo), end="")
        termo += razãodopa
        cont += 1
        add = int(input("\nQuantos termos você quer mostrar a mais? "))
