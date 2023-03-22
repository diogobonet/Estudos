peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print("O seu IMC é {:.2f}, você está abaixo do peso!" .format(imc))

elif (imc > 18.5) and (imc <= 25):
    print("O seu IMC é {:.2f}, você está com o peso normal!" .format(imc))

elif (imc > 25) and (imc <= 30):
    print("O seu IMC é {:.2f}, você está acima do peso!" .format(imc))

else:
    print("O seu IMC é {:.2f}, você está obeso!" .format(imc))
#fim