aluno = {}
aluno["nome"] = input("Nome: ")
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))
if aluno["media"] >= 7.0:
    aluno["Situação"] = "APROVADO!"
if aluno["media"] <= 3.0:
    aluno["Situação"] = "REPROVADO!"
if aluno["media"] < 7.0:
    aluno["Situação"] = "RECUPERAÇÃO"
print("=-"*55)
for k, v in aluno.items():
    print(f"{k} é igual a {v}")
   
