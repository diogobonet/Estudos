print("Jogo - Pedra, papel ou tesoura!")
pontos = int(input("Jogadores quantos pontos para vencer? "))

for i in range(pontos):
    j1 = str(input("Pedra, papel ou tesoura - Jogador 1: "))
    j2 = str(input("Pedra, Papel ou Tesoura - Jogador 2: "))
    if j1 == "Pedra" and j2 == "Tesoura":
        print("Jogador 1 Venceu!")
    elif j1 == "Tesoura" and j2 == "Papel":
        print("Jogador 1 Venceu!")
    elif j1 == "Papel" and j2 == "Pedra":
        print("Jogador 1 Venceu!")
    
    if j2 == "Pedra" and j1 == "Tesoura":
        print("Jogador 2 Venceu!")
    elif j2 == "Tesoura" and j1 == "Papel":
        print("Jogador 2 Venceu!")
    elif j2 == "Papel" and j1 == "Pedra":
        print("Jogador 2 Venceu!")
    
    if j1 == "Pedra" and j2 == "Pedra":
        print("Deu EMPATE!")
    if j1 == "Papel" and j2 == "Papel":
        print("Deu EMPATE!")
    if j1 == "Tesoura" and j2 == "Tesoura":
        print("Deu EMPATE!")
