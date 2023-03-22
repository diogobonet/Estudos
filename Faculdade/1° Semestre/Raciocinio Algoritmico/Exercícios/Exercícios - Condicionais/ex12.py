# PAR OU IMPAR
j1 = str(input("Jogador 1 escolha uma opção: (Par ou Impar) "))
j1a = int(input("Jogador 1 digite um número de 1 a 5: "))
j2 = int(input("Jogador 2 digite um número de 1 a 5: "))

if j1 == "Par":
    resultado = (j1a + j2) % 2  
    if resultado == 0:
        print("O jogador 1 ganhou!")
    if resultado == 1:
        print("O jogador 2 ganhou!")

if j1 == "Impar":
    resultado = (j1a + j2) % 2  
    if resultado == 1:
        print("O jogador 1 ganhou!")
    if resultado == 0:
        print("O jogador 2 ganhou!")
