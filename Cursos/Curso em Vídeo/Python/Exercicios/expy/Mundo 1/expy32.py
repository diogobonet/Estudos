from datetime import date
ano = int(input("Que ano você quer analisar? Coloque 0 caso você queira analisar o ano atual digite 0!"))
ano_atual = 2022
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or  ano % 400 == 0:
    print("O ano {} é bissexto!" .format(ano))

else:
    print("O ano {} não é bissexto!" .format(ano))