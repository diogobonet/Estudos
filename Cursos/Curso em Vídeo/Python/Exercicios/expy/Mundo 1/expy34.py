sal = float(input("Digite o seu sálario: R$"))

if sal <= 1250:
    aumento = (sal + sal * 15 / 100)
    print("Você recebeu um abono de 15 porcento de final de ano, você passou a receber R${:.2f}" .format(aumento))

if sal >= 1251:
    aumento = (sal + sal * 10 / 100)
    print("Você recebeu um abono de 10 porcento de final de ano, você passou a receber R${:.2f}" .format(aumento))

else:
    print("Algo deu errado na operação. Tente novamente!")