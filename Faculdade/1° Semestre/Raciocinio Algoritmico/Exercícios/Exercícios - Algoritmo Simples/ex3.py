disciplina = str(input("Qual disciplina você quer ver sua média? "));
nota1 = float(input("Agora digite sua primeira nota: "));
nota2 = float(input("Agora digite sua segunda nota: "));
nota3 = float(input("Agora digite sua terceira nota: "));
nota4 = float(input("Agora digite sua quarta nota: "));
média = (nota1 + nota2 + nota3 + nota4) / 4
print("Sua média na disciplina de {} é {}!" .format(disciplina, média));