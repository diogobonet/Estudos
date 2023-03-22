question = str(input("Para aonde você irá viajar? (Norte, Nordeste, Centro-Oeste, Sul)\n"))

if question == "Norte":
    question2 = str(input("A viagem para o Norte será apenas de ida ou ida e volta? (Ida ou Ida e Volta)\n"))
    if question2 == "Ida":
        print("Você selecionou (Ida), portanto irá pagar R$500!")
    elif question2 == "Ida e Volta":
        print("Você selecionou (Ida e Volta), portanto irá pagar R$900!")

if question == "Nordeste":
    question2 = str(input("A viagem para o Nordeste será apenas de ida ou ida e volta? (Ida ou Ida e Volta)\n"))
    if question2 == "Ida":
        print("Você selecionou (Ida), portanto irá pagar R$350!")
    elif question2 == "Ida e Volta":
        print("Você selecionou (Ida e Volta), portanto irá pagar R$650!")

if question == "Centro-Oeste":
    question2 = str(input("A viagem para o Centro-Oeste será apenas de ida ou ida e volta? (Ida ou Ida e Volta)\n"))
    if question2 == "Ida":
        print("Você selecionou (Ida), portanto irá pagar R$350!")
    elif question2 == "Ida e Volta":
        print("Você selecionou (Ida e Volta), portanto irá pagar R$600!")

if question == "Sul":
    question2 = str(input("A viagem para o Sul será apenas de ida ou ida e volta? (Ida ou Ida e Volta)\n"))
    if question2 == "Ida":
        print("Você selecionou (Ida), portanto irá pagar R$300!")
    elif question2 == "Ida e Volta":
        print("Você selecionou (Ida e Volta), portanto irá pagar R$550!")
else:
    print("Valor Inválido! Algo deu errado tente novamente!")