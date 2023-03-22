n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))
n3 = float(input("Digite sua nota: "))
media = (n1 + n2 + n3) / 3
if media <= 5.0:
    print("Você foi reprovado!")
elif media >=5.0 and media < 7.0:
    print("Você precisa fazer RECUPERAÇÃO!")
elif media >= 7.0:
    print("Você foi aprovado!")