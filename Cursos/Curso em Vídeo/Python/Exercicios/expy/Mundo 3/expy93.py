jogador = {}
gols = []
jogador["nome"] = input("Digite o nome do jogador: ")
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
for p in range(jogador['partidas']):
    gols = int(input(f"Quantos gols o jogador fez na partida {p + 1}: "))
    gols.append(gols)
    print(gols)