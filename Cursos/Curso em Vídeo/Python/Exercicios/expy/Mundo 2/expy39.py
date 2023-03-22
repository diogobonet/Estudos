nasc = int(input("ANO DE NASCIMENTO: "))
ano = 2022 - nasc
if ano == 18:
    print("Quem nasceu em {} tem 18 anos em 2022!" .format(nasc))
    print("Você te que se alistar IMEDIATAMENTE!")
elif ano > nasc:
    print("Você ainda não tem idade para se alistar!")
    print("Você precisa ter 18 anos! Você tem apenas {} anos!" .format(ano))
elif ano < nasc:
    result = 18 - ano
    print(result)