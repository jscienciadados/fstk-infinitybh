from banco import BancoDados
from produto import Produto
from venda import Venda
from datetime import datetime

def menu():
    print("\n1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Quantidade")
    print("4. Remover Produto")
    print("5. Registrar Venda")
    print("6. Sair")

def main():
    banco = BancoDados()
    cursor = banco.conexao.cursor()

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            desc = input("Descrição: ")
            qtd = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            cursor.execute("INSERT INTO produtos (nome, descricao, quantidade, preco) VALUES (?, ?, ?, ?)",
                           (nome, desc, qtd, preco))
            banco.conexao.commit()
            print("Produto cadastrado!")

        elif opcao == "2":
            cursor.execute("SELECT * FROM produtos")
            for row in cursor.fetchall():
                print(row)

        elif opcao == "3":
            id_prod = int(input("ID do produto: "))
            nova_qtd = int(input("Nova quantidade: "))
            cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_qtd, id_prod))
            banco.conexao.commit()
            print("Quantidade atualizada.")

        elif opcao == "4":
            id_prod = int(input("ID do produto: "))
            cursor.execute("DELETE FROM produtos WHERE id = ?", (id_prod,))
            banco.conexao.commit()
            print("Produto removido.")

        elif opcao == "5":
            id_prod = int(input("ID do produto: "))
            qtd_venda = int(input("Quantidade vendida: "))
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO vendas (produto_id, quantidade, data) VALUES (?, ?, ?)",
                           (id_prod, qtd_venda, data))
            cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?", (qtd_venda, id_prod))
            banco.conexao.commit()
            print("Venda registrada!")

        elif opcao == "6":
            banco.fechar_conexao()
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
