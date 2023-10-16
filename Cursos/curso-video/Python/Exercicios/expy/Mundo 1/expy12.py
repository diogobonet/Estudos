valor = float(input("Digite o valor do produto: "))
desc = valor - (valor * 5 / 100)
print("O valor do produto era R${}, com desconto aplicado de 5% o valor passou a ser R${}" .format(valor, desc))