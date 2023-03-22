nota1 = float(input("Digite sua primeira nota: "));
nota2 = float(input("Digite sua segunda nota: "));
nota3 = float(input("Digite sua terceira nota: "));
nota4 = float(input("Digite sua quarta nota: "));
média = (nota1 + nota2 + nota3 + nota4) / 4
if (média >= 70):
    print("Você foi aprovado na disciplina de matematica com {} de média" .format(média))
else: 
    print("Você foi reprovado!")