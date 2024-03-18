km = int(input("Quantos kilometros você irá viajar? "))
if km <= 200:
    valor = km * 0.50
    print("Você irá fazer uma viagem que custa R${}" .format(valor))
else:
    valor = km * 0.45
    print("Você ira fazer uma viagem que custa R${}" .format(valor))