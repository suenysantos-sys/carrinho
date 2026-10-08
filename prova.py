class Produto:
    def __init__(self, nome, preco, descricao, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao
        self.__quantidade = quantidade

    # GETTERS

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_descricao(self):
        return self.__descricao

    def get_quantidade(self):
        return self.__quantidade

    # SETTERS

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade


class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                break

    def calcular_total(self):
        total = 0

        for produto in self.__produtos:
            total += produto.get_preco()

        return total

    def exibir_produtos(self):
        for produto in self.__produtos:
            print("Nome:", produto.get_nome())
            print("Preço:", produto.get_preco())
            print("Descrição:", produto.get_descricao())
            print("Quantidade:", produto.get_quantidade())



carrinho = CarrinhoDeCompras()

while True:
    print("\n--- MENU ---")
    print("1 - Incluir produto")
    print("2 - Excluir produto")
    print("3 - Visualizar carrinho")
    print("4 - Consultar total")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: ").replace(",", "."))
            descricao = input("Descrição: ")
            quantidade = int(input("Quantidade: "))

            produto = Produto(nome, preco, descricao, quantidade)
            carrinho.adicionar_produto(produto)

            print("Produto adicionado!")

        case "2":
            nome = input("Nome do produto que deseja remover: ")
            carrinho.remover_produto(nome)

        case "3":
            carrinho.exibir_produtos()

        case "4":
            total = carrinho.calcular_total()
            print("Total da compra:", total)

        case "5":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida!")