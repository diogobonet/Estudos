#EMPRESTIMO DO BANCO
valor = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário: R$"))
anos = int(input("Em quanto anos você irá pagar: "))

prestação = (anos * 12) / valor
minimo = (salario * 30) / 100

if prestação <= minimo:
    print("Emprestimo foi APROVADO!")
elif prestação >= minimo:
    print("O emprestimo foi NEGADO!")