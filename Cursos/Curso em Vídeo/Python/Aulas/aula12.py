nome = str(input("Qual o seu nome? "))
print("Bom dia {}" .format(nome))
if nome == "Diogo":
    print("Que nome lindo! ")
elif nome == 'Pedro' or nome == 'Maria':
    print("Seu nome é bem popular no Brasil!")
elif nome in 'Rogerio Claudio Jéssica':
    print("O nome de vocês é bem legal!")
else:
    print("Vocês possuem o nome super normal!")
# ESTRUTURA CONDICIONAL ANINHADA. 