import menu
from menu import menuprincipal
import dicperson
import random

chance = 9
personalidade = random.choice([dicperson.pessoa1, dicperson.pessoa2, dicperson.pessoa3, ...])

def game(chance):
    dica = input("Escolha um número de 1 a 10 para a dica -> ")
    dicasPegas = {} # Lista para armazenar as dicas já pegas
    if dica in dicasPegas:
        print("Essa dica já foi pega")
        return
    else:
        for _ in range(10):
            if chance <= 10 and chance > 0:
                returnDica = personalidade.get(dica)
                print(f"Dica [{dica}]: ", returnDica)
                dicasPegas[dica] = True
                menugame(chance)
            if chance == 0:
                print("Você perdeu o jogo!")

def menugame(chance):
    print("[1] Tentar acertar")
    print("[2] Pedir uma dica")
    op = int(input("-> "))
    if op == 1:
        chute(chance)
    if op == 2:
        print(f"Você pegou outra dica! Você ainda possui {chance} chances para acertar!")
        chance -= 1 # Atualiza o número de chances
        game(chance)

def chute(chance):
    chute = input("Digite o nome da personalidade (para voltar digite 0) -> ")
    nome = personalidade["nome"]
    if chute == "0":
        return game(chance)
    if chute != nome:
        chance = chance - 1
        print(f"Você errou! Você ainda possui {chance} chances!")
    if chute == nome:
        print("Parabéns! Você acertou!")
        print(f"A personalidade era [{nome}]")
        print("Você deseja continuar jogando? [S/N]")
        escolha = input("-> ")
        if escolha == "S" or escolha == "s" or escolha == "sim":
            menu.menuprincipal()
        if escolha == "N" or escolha == "n" or escolha == "não":
            exit()