# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 21:45:02 2024

Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo 
determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, 
representando o início e o fim do intervalo (inclusive).

Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. 
Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

Ao final, exiba a soma dos números pares encontrados.

@author: Gateway
"""

# Solicita ao usuário que insira o início e o fim do intervalo
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Inicializa a soma dos números pares
soma_pares = 0

# Verifica se o intervalo é válido
if inicio > fim:
    print("O início do intervalo não pode ser maior que o fim.")
else:
    # Itera sobre o intervalo de números
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            soma_pares += numero
    else:
        # Verifica se houve algum número par somado
        if soma_pares == 0:
            print("Não há números pares no intervalo.")
    print(f'A soma dos pares {inicio} e {fim} = ',soma_pares)