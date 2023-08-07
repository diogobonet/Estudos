import menu
from menu import menuprincipal
import dicperson
import random
import sys
import time

chance = 10
personalidade = random.choice([dicperson.pessoa1, dicperson.pessoa2, dicperson.pessoa3, dicperson.pessoa4, dicperson.pessoa5, dicperson.pessoa6, dicperson.pessoa7, dicperson.pessoa8, dicperson.pessoa9, dicperson.pessoa10, ...])

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BOLD = "\033[1m"
BLUE = "\033[34m"

def game(chance):
    dica = input("Escolha um número de 1 a 10 para a dica -> ")
    nome = personalidade["nome"]
    if (dica == nome):
        print("ERRO! Para digitar um nome selecione a opção [1]")
    elif (dica == ""):
        print("ERRO! Você precisa pegar alguma dica!")
        return game()
    else:
        for _ in range(10):
            if chance <= 10 and chance > 0:
                returnDica = personalidade.get(dica)
                print(f"Dica [{dica}]: ", returnDica)
                menugame(chance)
            elif chance == 0:
                print(RED + f"Você perdeu o jogo! \nA personalidade era [{nome}]!" + RESET)
                return menu.menuprincipal()

def menugame(chance):
    print("[1] Tentar acertar")
    print("[2] Pedir uma dica")
    op = int(input("-> "))
    match op:
        case 1:
            chute(chance)
        case 2:
            print("Você pegou outra dica! Você ainda possui" + BOLD + f" {chance} " + RESET + "chances para acertar!")
            chance -= 1  # Atualiza o número de chances
            game(chance)
        case 3:
            opt = input(RED + "Você realmente quer sair do jogo?" + RESET)

        case _:
            return game()


def chute(chance):
    chute = input("Digite o nome da personalidade (para voltar digite 0) -> ")
    nome = personalidade["nome"]
    if chute == "0":
        return game(chance)
    if chute != nome:
        chance -= 1
        print(RED + f"Você errou! Você ainda possui {chance} chances!" + RESET)
    if chute == nome:
        print(GREEN + "Parabéns! Você acertou!")
        print(f"A personalidade era [{nome}]" + RESET)
        time.sleep(5)
        return menu.menuprincipal()


