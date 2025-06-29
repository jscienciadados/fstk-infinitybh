class Produto:
    def __init__(self, nome, descricao, quantidade, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
