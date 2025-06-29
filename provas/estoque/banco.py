import sqlite3

class BancoDados:
    def __init__(self, nome_banco='estoque.db'):
        self.conexao = sqlite3.connect(nome_banco)
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY(produto_id) REFERENCES produtos(id)
            )
        ''')
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
