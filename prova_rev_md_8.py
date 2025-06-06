import os

def listar_conteudo_diretorio_atual():
  """
  Lista e exibe todos os arquivos e pastas presentes no diretório
  onde o script Python está sendo executado.
  """
  try:
    # Obtém o caminho do diretório atual onde o script está sendo executado
    # Esta linha é opcional, pois listdir() sem argumentos lista o diretório atual
    diretorio_atual = os.getcwd()
    print(f"Listando conteúdo do diretório: {diretorio_atual}\n")

    # Usa os.listdir() para obter uma lista de arquivos e pastas
    conteudo_do_diretorio = os.listdir()

    # Verifica se o diretório está vazio
    if not conteudo_do_diretorio:
      print("O diretório atual está vazio.")
      return

    # Itera sobre a lista e exibe cada item individualmente
    for item in conteudo_do_diretorio:
      print(item)

  except OSError as e:
    print(f"Erro ao acessar o diretório: {e}")
  except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

# Chama a função para executar a listagem
listar_conteudo_diretorio_atual()