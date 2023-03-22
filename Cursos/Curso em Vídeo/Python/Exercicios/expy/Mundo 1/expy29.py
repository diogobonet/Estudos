vel_atual = int(input("Qual velocidade atual do seu carro?\n"))

if vel_atual <= 80:
    print("Dirija com segurança! Tenha um bom dia!")
else:
    print("MULTADO! Você ultrapassou o limite de velocidade de 80km/h.")
    print("Por isso você terá que pagar uma multa de R${}" .format((vel_atual - 80) * 7))
