valor = float(input("Informe o valor do produto R$"))
pagamento = str(input("Informe a forma de pagamento: (dinheiro, cheque, cartão, 2x sem juros, 2x com juros!) "))

if pagamento == "dinheiro":
    desconto = valor - (valor * 10 / 100)
    print("O valor do produto inicial era R${:.2f}, com desconto aplicado de 10% passa a ser R${}" .format(valor, desconto))
elif pagamento == "cheque":
    desconto = valor - (valor * 10 / 100)
    print("O valor do produto inicial era R${:.2f}, com desconto aplicado de 10% passa a ser R${}" .format(valor, desconto))

if pagamento == "cartão":
    desconto = valor - (valor * 15 / 100)
    print("O valor do produto inicial era R${:.2f}, com desconto aplicado de 15% passa a ser R${}" .format(valor, desconto))

if pagamento == "2x sem juros":
    desconto = (valor / 2)
    print("Você pagará R${:.2f} em duas parcelas de R${:.2f} sem juros!".format(valor, desconto))

if pagamento == "2x com juros":
    desconto = (valor + valor *10/100) / 2
    print("Você pagará R${:.2f} em duas parcelas de R${:.2f} com juros!".format(valor, desconto))