def maior_numero(num1, num2, num3):
  """
  Compara três números e retorna o maior entre eles.

  Argumentos:
    num1 (int/float): O primeiro número.
    num2 (int/float): O segundo número.
    num3 (int/float): O terceiro número.

  Retorna:
    (int/float): O maior número entre os três.
  """
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

# Testando a função com alguns exemplos:
print(f"O maior número entre 10, 5 e 8 é: {maior_numero(10, 5, 8, 22, -57, 1.0)}")
