# main.py

import os
from gerenciador_alunos import adicionar_aluno, remover_aluno, atualizar_aluno, ver_alunos

def menu():
    """Exibe o menu principal e gerencia as interações do usuário."""
    alunos = {}
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' Gerenciador de Alunos '.center(40, '='))
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")
        print('=' * 40)

        escolha = input("Selecione uma opção -> ")

        match escolha:
            case '1':
                adicionar_aluno(alunos)
            case '2':
                remover_aluno(alunos)
            case '3':
                atualizar_aluno(alunos)
            case '4':
                ver_alunos(alunos)
            case '5':
                print("Saindo do gerenciador de alunos.")
                break
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()