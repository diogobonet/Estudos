# nome = input("Digite o seu nome: ")
# for i in range(nome):
#   # print(i)

soma = 0 
for i in range(3):
    num = int(input("Digite {}° o número: " .format(str(i + 1))))
    soma += num
print(soma)