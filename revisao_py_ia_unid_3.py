# Cria um dicionário vazio para armazenar os produtos e seus preços
produtos = {}

print("Por favor, insira o nome e o preço de cinco produtos:")

# Loop para coletar informações de cinco produtos
for i in range(1, 6): # Loop de 1 a 5 para contar os produtos
    print(f"\nProduto {i}:")
    nome_produto = input("Nome do produto: ")

    while True: # Loop para garantir que o preço seja um número válido
        try:
            preco_produto = float(input("Preço do produto (ex: 10.50): "))
            if preco_produto < 0:
                print("O preço não pode ser negativo. Por favor, insira um valor válido.")
            else:
                break # Sai do loop se o preço for um número positivo
        except ValueError:
            print("Entrada inválida. Por favor, insira um número para o preço.")

    # Adiciona o produto e seu preço ao dicionário
    produtos[nome_produto] = preco_produto

# Calcula o valor total da compra
valor_total_compra = 0
for preco in produtos.values():
    valor_total_compra += preco

# Exibe o valor total da compra
print("\n--- Resumo da Compra ---")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}") # Formata o preço com 2 casas decimais

print(f"\nValor Total da Compra: R$ {valor_total_compra:.2f}")