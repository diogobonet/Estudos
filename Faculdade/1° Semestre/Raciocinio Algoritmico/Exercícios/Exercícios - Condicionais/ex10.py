sexo = str(input("Qual é o seu sexo? (h/m) "))
h = float(input("Qual é a sua altura? "))

if sexo == "h":
     calculo = ((72.7 * h) - 58);
     print("O peso ideal para você é de {:.2f}kg!" .format(calculo))
elif sexo == "m":
     calculo = ((62.1 * h) - 44.7)
     print("O peso ideal para você é de {:.2f}kg!" .format(calculo))
else:
     print("Algo deu errado!")