# Lista global para armazenar todas as tarefas
tarefas = []
proximo_id = 1 # Para garantir que cada tarefa tenha um ID único

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista de tarefas."""
    global proximo_id
    print("\n--- Adicionar Nova Tarefa ---")
    nome = input("Nome da tarefa: ").strip()
    if not nome:
        print("O nome da tarefa não pode ser vazio. Tarefa não adicionada.")
        return

    descricao = input("Descrição (opcional): ").strip()

    while True:
        prioridade = input("Prioridade (Baixa, Média, Alta): ").strip().capitalize()
        if prioridade in ["Baixa", "Média", "Alta"]:
            break
        else:
            print("Prioridade inválida. Escolha entre Baixa, Média ou Alta.")

    categoria = input("Categoria (ex: Casa, Trabalho, Estudo): ").strip().capitalize()
    if not categoria:
        categoria = "Geral" # Categoria padrão

    tarefa = {
        "id": proximo_id,
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    proximo_id += 1
    print(f"Tarefa '{nome}' adicionada com sucesso! (ID: {tarefa['id']})")

def listar_tarefas(lista_para_exibir=None):
    """Exibe todas as tarefas ou uma lista filtrada."""
    if lista_para_exibir is None:
        lista_para_exibir = tarefas

    if not lista_para_exibir:
        print("\nNenhuma tarefa para exibir.")
        return

    print("\n--- Suas Tarefas ---")
    for tarefa in lista_para_exibir:
        status = "✓ Concluída" if tarefa["concluida"] else "✗ Pendente"
        print(f"ID: {tarefa['id']} | Nome: {tarefa['nome']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']} | Status: {status}")
        if tarefa["descricao"]:
            print(f"  Descrição: {tarefa['descricao']}")
        print("-" * 30)

def marcar_como_concluida():
    """Marca uma tarefa existente como concluída."""
    listar_tarefas() # Mostra as tarefas para o usuário escolher o ID
    if not tarefas:
        return

    while True:
        try:
            tarefa_id = int(input("\nDigite o ID da tarefa para marcar como concluída: "))
            break
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

    encontrada = False
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = True
            print(f"Tarefa '{tarefa['nome']}' marcada como concluída!")
            encontrada = True
            break
    if not encontrada:
        print(f"Tarefa com ID {tarefa_id} não encontrada.")

def exibir_por_prioridade():
    """Exibe tarefas filtradas por prioridade."""
    prioridades_validas = ["Baixa", "Média", "Alta"]
    while True:
        prioridade_filtro = input("Digite a prioridade para filtrar (Baixa, Média, Alta): ").strip().capitalize()
        if prioridade_filtro in prioridades_validas:
            break
        else:
            print("Prioridade inválida. Escolha entre Baixa, Média ou Alta.")

    tarefas_filtradas = [t for t in tarefas if t["prioridade"] == prioridade_filtro]
    listar_tarefas(tarefas_filtradas)

def exibir_por_categoria():
    """Exibe tarefas filtradas por categoria."""
    categoria_filtro = input("Digite a categoria para filtrar: ").strip().capitalize()
    if not categoria_filtro:
        print("A categoria não pode ser vazia.")
        return

    tarefas_filtradas = [t for t in tarefas if t["categoria"] == categoria_filtro]
    listar_tarefas(tarefas_filtradas)

def remover_tarefa():
    """Remove uma tarefa da lista."""
    listar_tarefas()
    if not tarefas:
        return

    while True:
        try:
            tarefa_id = int(input("\nDigite o ID da tarefa que deseja remover: "))
            break
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

    tarefa_removida = False
    for i, tarefa in enumerate(tarefas):
        if tarefa["id"] == tarefa_id:
            nome_removido = tarefas.pop(i)["nome"] # Remove e pega o nome
            print(f"Tarefa '{nome_removido}' removida com sucesso!")
            tarefa_removida = True
            break
    if not tarefa_removida:
        print(f"Tarefa com ID {tarefa_id} não encontrada.")

def listar_categorias_existentes():
    """Lista todas as categorias únicas atualmente em uso pelas tarefas."""
    if not tarefas:
        print("\nNenhuma tarefa cadastrada para listar categorias.")
        return
    
    categorias = set() # Usamos um conjunto para armazenar categorias únicas
    for tarefa in tarefas:
        categorias.add(tarefa["categoria"])
    
    if categorias:
        print("\n--- Categorias Existentes ---")
        for categoria in sorted(list(categorias)): # Ordena e exibe as categorias
            print(f"- {categoria}")
    else:
        print("\nNenhuma categoria encontrada.")

def menu_principal():
    """Exibe o menu principal e gerencia a interação do usuário."""
    while True:
        print("\n" + "="*30)
        print("  GERENCIADOR DE TAREFAS")
        print("="*30)
        print("1. Adicionar Tarefa")
        print("2. Listar Todas as Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Remover Tarefa")
        print("7. Listar Categorias Existentes")
        print("8. Sair")
        print("-" * 30)

        escolha = input("Escolha uma opcão: ").strip()

        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            marcar_como_concluida()
        elif escolha == '4':
            exibir_por_prioridade()
        elif escolha == '5':
            exibir_por_categoria()
        elif escolha == '6':
            remover_tarefa()
        elif escolha == '7':
            listar_categorias_existentes()
        elif escolha == '8':
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executa o menu principal quando o script é iniciado
if __name__ == "__main__":
    menu_principal()