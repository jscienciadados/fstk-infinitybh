def media(num1, num2, num3):
  """
  Calcula a média aritmética de três números.

  Args:
    num1: O primeiro número.
    num2: O segundo número.
    num3: O terceiro número.

  Returns:
    A média aritmética dos três números.
  """
  soma = num1 + num2 + num3
  resultado_media = soma / 3
  return resultado_media

print(media(5, 10, 15))