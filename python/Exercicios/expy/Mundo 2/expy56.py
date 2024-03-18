somaIdade = 0
mediaidade = 0
for c in range(4):
    print("------- PESSOA {}--------" .format(str(c+1)))
    nome = input("NOME: ").strip()
    idade = int(input("IDADE: "))
    sexo = input("SEXO [M/F]: ").strip()
    somaIdade += idade
mediaidade = somaIdade / 4
print("A média das idade somadas é de: ", mediaidade)