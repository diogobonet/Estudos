prod = str(input("Digite o nome do produto: "))
quant = int(input("Quantos produtos você quer: "))
valor = float(input("Digite o valor do produto: "))
total = valor * quant
print("Você irá pagar R${:.2f} pelo(a) {}!" .format(total, prod))