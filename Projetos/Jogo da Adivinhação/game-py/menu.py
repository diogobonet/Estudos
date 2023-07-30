RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
def menuprincipal():
    while True:
        try:
            print("="*25); print(BLUE + " Advinhe a Personalidade " + RESET); print("="*25);
            print(GREEN + "[1] Começar um novo jogo")
            print(RED + "[2] Sair" + RESET)
            op = int(input("-> "))
            if (op == 1):
                import jogo
                return jogo.game(9)
                pass
            if (op == 2):
                menubreak()
        except:
            print("Opção inválida! Tente novamente!")

def menubreak():
    import sys
    sys.exit()