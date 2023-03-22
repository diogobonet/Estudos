prod = str(input("Digite o nome do produto: "))
quant = int(input("Quantos produtos você quer: "))
valor = float(input("Digite o valor do produto (para pagamento á vista desconto de 15%): R$"))
total = valor * quant
desc = total - (total * 15 / 100)
print("Você irá pagar R${:.2f} pelo(a) {} com desconto aplicado!" .format(desc, prod))