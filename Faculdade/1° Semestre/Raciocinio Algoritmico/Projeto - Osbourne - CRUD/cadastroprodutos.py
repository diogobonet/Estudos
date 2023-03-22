import time

# Cadastrar um Jogo/Produto
def cadProd():
    print("="*55)
    print("                Cadastro de Produtos")
    print("=" * 55)
    nomeProduto = input("Digite o nome do Jogo: ")
    descProduto = input("Digite a descrição do produto: ")
    categoria = input("Selecione a categoria do jogo:")
    valor = float(input("Digite o preço do jogo - R$"))
    empresa = input(f"Digite o nome da empresa que desenvolveu o jogo ({nomeProduto}): ")
    cadastroJogo = {"NomeProd": nomeProduto, "DescProduto": descProduto, "Preço": valor, "Desenvolvedor": empresa,
                    "Categoria": categoria}
    print(cadastroJogo)
    print("Cadastrando produto...")
    time.sleep(2)

# Excluir produto
def excProd():
    pass

# Editar Produto
def editarProd():
    pass

def menuprod():
    while True:
        print("=" * 55)
        print("                Setor de Produtos")
        print("=" * 55)
        print("[ 1 ] Cadastrar Jogo/Produto")
        print("[ 2 ] Editar Jogo/Produto")
        print("[ 3 ] Excluir Jogo/Produto")
        op = int(input("Escolha uma opção:\n"))
        if op == 1:
            cadProd()
            break