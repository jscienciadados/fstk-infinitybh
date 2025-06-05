# Cria um dicionário vazio para armazenar as informações do contato
contato = {}

# Solicita ao usuário para fornecer o nome do contato
nome = input("Por favor, insira o nome do contato: ")
contato["nome"] = nome

# Solicita ao usuário para fornecer o número de telefone
telefone = input("Por favor, insira o número de telefone: ")
contato["telefone"] = telefone

# Solicita ao usuário para fornecer o endereço de email
email = input("Por favor, insira o endereço de email: ")
contato["email"] = email

# Exibe o conteúdo do dicionário
print("\nInformações do Contato:")
for chave, valor in contato.items():
    print(f"{chave.capitalize()}: {valor}")