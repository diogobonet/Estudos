print("Gerador de PA")
print("-="*15)
primeirotermo = int(input("Primeiro termo:"))
razãodopa = int(input("Razão do PA: "))
cont = 1
termo = primeirotermo
while cont <= 10:
    print("{} -> ".format(termo), end="")
    termo += razãodopa
    cont += 1