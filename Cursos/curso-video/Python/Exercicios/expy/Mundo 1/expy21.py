nome = str(input("Digite o seu nome completo: "))
print("Analisando seu nome...")
print("O seu nome em maiscúlas é {}" .format(nome.upper()))
print("O seu nome em minuscúlas é {}" .format(nome.lower()))
print("O seu nome possui {} letras!" .format(len(nome) - nome.count(" ")))
separa = nome.split()
print("Seu primeiro nome é {}, ele tem {} letras!" .format(separa[0], len(separa[0])))