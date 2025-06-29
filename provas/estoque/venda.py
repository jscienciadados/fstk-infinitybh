class Venda:
    def __init__(self, produto_id, quantidade, data, id=None):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.data = data
