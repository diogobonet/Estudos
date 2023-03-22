import time
import menu
# Menu da Loja
print("="*55)
print("                        Loja")
print("=" * 55)
def lojinha():
    while True:
        print("[ 1 ] Procurar jogos")
        print("[ 2 ] Jogos indicados")
        print("[ 3 ] Metodos de pagamentos")
        print("[ 4 ] Voltar para Menu")
        op = int(input("Escolha uma opção:\n"))
        if op == 1:
            procurar = input("Pesquisar jogo: ")
        if op == 2:
            pass
        if op == 3:
            print("Os métodos de pagamentos da loja são: Boleto, Pix, Cartão de Débito")
            time.sleep(4)
        if op == 4:
            menu.menu()
