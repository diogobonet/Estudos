sexo = str(input("Informe seu sexo:[M/F] ")).upper()

while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).upper()
print("Sexo {} registrado com sucesso.".format(sexo))