print("Operações Númericas!")
num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))
op = input("Qual operação você deseja realizar?\n(+, -, *, /, **)")

if op == "+":
    resul = num1 + num2
    print("A operação é {} + {}= {}" .format(num1, num2, resul))

if op == "-":
    resul = num1 - num2
    print("A operação é {} - {}= {}" .format(num1, num2, resul))

if op == "*":
    resul = num1 * num2
    print("A operação é {} * {}= {}" .format(num1, num2, resul))

if op == "/":
    resul = num1 / num2
    print("A operação é {} / {}= {}" .format(num1, num2, resul))

if op == "**":
    resul = num1 ** num2
    print("A operação é {} ** {}= {}" .format(num1, num2, resul))

else:
    print("Algo deu errado na sua operação! Tente novamente!")