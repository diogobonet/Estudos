import menu
from menu import menuprincipal
import dicperson
import random
import sys

chance = 10
personalidade = random.choice([dicperson.pessoa1, dicperson.pessoa2, dicperson.pessoa3, dicperson.pessoa4, ...])

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BOLD = "\033[1m"
BLUE = "\033[34m"

def game(chance):
    dica = input("Escolha um número de 1 a 10 para a dica -> ")
    dicasPegas = {} # Lista para armazenar as dicas já pegas
    if dica in dicasPegas:
        print("Você já pegou essa dica! Pegue outra!")
        return
    else:
        for _ in range(10):
            nome = personalidade["nome"]
            if chance <= 10 and chance > 0:
                returnDica = personalidade.get(dica)
                print(f"Dica [{dica}]: ", returnDica)
                dicasPegas[dica] = True
                menugame(chance)
            if chance == 0:
                print(f"Você perdeu o jogo! A personalidade era {nome}!")
                return menu.menuprincipal()

def menugame(chance):
    print("[1] Tentar acertar")
    print("[2] Pedir uma dica")
    op = int(input("-> "))
    if op == 1:
        chute(chance)
    if op == 2:
        print("Você pegou outra dica! Você ainda possui" + BOLD + f" {chance} "+ RESET+ "chances para acertar!")
        chance -= 1 # Atualiza o número de chances
        game(chance)

def chute(chance):
    chute = input("Digite o nome da personalidade (para voltar digite 0) -> ")
    nome = personalidade["nome"]
    if chute == "0":
        return game(chance)
    if chute != nome:
        chance = chance - 1
        print(RED + f"Você errou! Você ainda possui {chance} chances!" + RESET)
    if chute == nome:
        print(GREEN + "Parabéns! Você acertou!")
        print(f"A personalidade era [{nome}]" + RESET)
        return menu.menuprincipal()


