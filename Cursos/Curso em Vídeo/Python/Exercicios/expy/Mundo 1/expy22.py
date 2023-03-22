num = int(input("Digite um números: "))
print("Analisando o número {}..." .format(num))
uni = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print("Unidade: {}" .format(uni))
print("Dezena: {}" .format(dezena))
print("Centena: {}" .format(centena))
print("Milhar: {}" .format(milhar))