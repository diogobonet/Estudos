from random import randint
print("Sou seu computador.")
print("Acabei de pensar em número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
computador = randint(0, 10)
acertou = False
quant = 0
while not acertou:
    tent = int(input("Qual é seu palpite?\n"))
    quant += 1
    if tent == computador:
        acertou = True
    else:
        if tent < computador:
            print("Mais... Tente mais uma vez.")
        elif tent > computador:
            print("Menos... Tente mais uma vez.")
print("Você acertou. O número que eu escolhi foi {}! Você tentou {} vezes para acertar!" .format(computador, quant))