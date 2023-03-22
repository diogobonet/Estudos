d1 = int(input("Digite primeiro digito do CPF: "))
d2 = int(input("Digite o segundo digito do CPF: "))
d3 = int(input("Digite o terceiro digito do CPF: "))
d4 = int(input("Digite o quarto digito do CPF: "))
d5 = int(input("Digite o quinto digito do CPF: "))
d6 = int(input("Digite o sexto digito do CPF: "))
d7 = int(input("Digite o setimo digito do CPF: "))
d8 = int(input("Digite o oitavo digito do CPF: "))
d9 = int(input("Digite o nono digito do CPF: "))
d10 = int(input("Digite o decimo digito do CPF: "))
d11 = int(input("Digite o decimo primeiro digito do CPF: "))

#Calculo Primeiro digito
calculo1 = d1 * 10 + d2 * 9 + d3 * 8 + d4 * 7 + d5 * 6 + d6 * 5 + d7 * 4 + d8 * 3 + d9 * 2
calculo2 = (calculo1 * 10) % 11
# Calculo - Segundo digito
calculo3 = d1 * 11 + d2 * 10 + d3 * 9 + d4 * 8 + d5 * 7 + d6 * 6 + d7 * 5 + d8 * 4 + d9 * 3 + d10 * 2
calculo4 = (calculo3 * 10) % 11

if calculo2 == d10:
    print("O primeiro digito está correto na validação!")

if calculo4 == d11:
    print("O segundo digito está correto na validação!")

if calculo2 == 10:
    d10 = int(0)

if calculo4 == 10:
    d11 = int(0)

if calculo2 == d10 and calculo4 == d11:
    print("O seu CPF é válido!")

else:
    print("CPF inválido!")