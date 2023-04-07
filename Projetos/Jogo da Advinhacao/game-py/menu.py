def menuprincipal():
    while True:
        try:
            print("="*25); print("Advinhe a Personalidade"); print("="*25);
            print("[1] Começar um novo jogo")
            print("[2] Sair")
            op = int(input("-> "))
            if (op == 1):
                import jogo
                return jogo.game(9)
            if (op == 2):
                break
        except:
            print("Opção inválida! Tente novamente!")
