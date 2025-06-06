import random

def lancar_dados():
  """
  Simula o lançamento de dois dados e retorna a soma dos resultados.
  Cada dado gera um número aleatório entre 1 e 6.
  """
  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  total = dado1 + dado2
  return total

# Exemplo de uso da função:
resultado = lancar_dados()
print(f"O resultado do lançamento dos dados é: {resultado}")