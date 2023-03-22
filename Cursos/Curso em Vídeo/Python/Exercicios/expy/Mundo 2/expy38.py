num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print("O PRIMEIRO número é maior")
elif num2 > num1:
    print("O SEGUNDO número é maior")
elif num1 == num2:
    print("Os DOIS números são IGUAIS")
else:
    print("ALGO DEU ERRADO! TENTE NOVAMENTE!")