import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

def criar_banco_de_dados():
    

    # Criar tabela de produtos
    cursor.execute('''
        CREATE TABLE produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            descricao TEXT,
            quantidade INTEGER,
            preco REAL
        )
    ''')

    # Criar tabela de vendas
    cursor.execute('''
        CREATE TABLE vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER,
            quantidade INTEGER,
            data DATE,
            FOREIGN KEY(produto_id) REFERENCES produtos(id)
        )
    ''')

# criando o método para adicionar produto
def adicionar_produto(self, nome, descricao, quantidade, preco):
        """Adiciona um novo produto ao estoque.

        Args:
            nome (str): Nome do produto.
            descricao (str): Descrição do produto.
            quantidade (int): Quantidade inicial em estoque.
            preco (float): Preço unitário do produto.
        """

        try:
            self.cursor.execute("INSERT INTO produtos (nome, descricao, quantidade, preco) VALUES (?, ?, ?, ?)",
                               (nome, descricao, quantidade, preco))
            self.conn.commit()
            print("Produto adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao adicionar produto: {e}")

# método para adcionar uma venda
def registrar_venda(self, produto_id, quantidade, data):
        """Registra uma nova venda.

        Args:
            produto_id (int): ID do produto vendido.
            quantidade (int): Quantidade vendida.
            data (str): Data da venda no formato 'YYYY-MM-DD'.
        """

        try:
            # Inserir a venda
            self.cursor.execute("INSERT INTO vendas (produto_id, quantidade, data) VALUES (?, ?, ?)",
                               (produto_id, quantidade, data))

            # Atualizar a quantidade em estoque
            self.cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?",
                               (quantidade, produto_id))

            self.conn.commit()
            print("Venda registrada com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao registrar venda: {e}")

# método para excluir um produto
def excluir_produto(self, produto_id):
        """Exclui um produto pelo seu ID.

        Args:
            produto_id (int): O ID do produto a ser excluído.
        """
        try:
            self.cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
            self.conn.commit()
            print("Produto excluído com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao excluir produto: {e}") 

# Gerando o relatorio de produtos
def gerar_relatorio_produtos(self):
        """Gera um relatório completo dos produtos, incluindo valor total em estoque."""
        self.cursor.execute("""
            SELECT nome, descricao, quantidade, preco, quantidade * preco AS valor_total
            FROM produtos
        """)
        produtos = self.cursor.fetchall()

        print("\nRelatório de Produtos:")
        print("-" * 80)
        print(f"| {'Nome':<20} | {'Descrição':<30} | {'Quantidade':^10} | {'Preço':^10} | {'Valor Total':^10} |")
        print("-" * 80)
        for produto in produtos:
            print(f"| {produto[0]:<20} | {produto[1]:<30} | {produto[2]:^10} | R${produto[3]:^10,.2f} | R${produto[4]:^10,.2f} |")
        print("-" * 80)                                   
    

conn.commit()


if __name__ == "__main__":
    criar_banco_de_dados()
    print("Banco de dados 'loja.db' criado com sucesso!")
    def selecionar_produto(self, produto_id=None):
        """Seleciona informações de um produto.

        Args:
            produto_id (int, optional): ID do produto a ser selecionado.
                Se não for informado, retorna todos os produtos.
        """
        if produto_id:
            query = "SELECT nome, descricao, quantidade FROM produtos WHERE id = ?"
            params = (produto_id,)
        else:
            query = "SELECT nome, descricao, quantidade FROM produtos"
            params = ()

        self.cursor.execute(query, params)
        produtos = self.cursor.fetchall()

        if produtos:
            for produto in produtos:
                print(f"Nome: {produto[0]}\nDescrição: {produto[1]}\nQuantidade: {produto[2]}")
        else:
            print("Produto não encontrado.")
    conn.close()