dias = int(input("Quantos dias você utilizou o carro?\n"))
km = float(input("Quantos kilometros você rodou com o carro?\n"))
calculo1 = dias * 60
calculo2 = km * 0.15
total = calculo1 + calculo2
print("O valor total é de R${}!" .format(total))