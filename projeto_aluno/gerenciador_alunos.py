# gerenciador_alunos.py

def adicionar_aluno(alunos):
    """Solicita ao usuário que adicione um aluno ao dicionário."""
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    
    if matricula in alunos:
        print("Aluno já cadastrado com essa matrícula.")
    else:
        alunos[matricula] = nome
        print(f"Aluno '{nome}' adicionado com sucesso!")

def remover_aluno(alunos):
    """Solicita ao usuário que remova um aluno do dicionário."""
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    
    if matricula in alunos:
        del alunos[matricula]
        print(f"Aluno com matrícula {matricula} removido com sucesso!")
    else:
        print("Matrícula não encontrada.")

def atualizar_aluno(alunos):
    """Solicita ao usuário que atualize o nome de um aluno no dicionário."""
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print(f"Nome do aluno com matrícula {matricula} atualizado para '{novo_nome}'.")
    else:
        print("Matrícula não encontrada.")

import time

def ver_alunos(alunos):
    """Lista todos os alunos cadastrados no dicionário e exibe por 10 segundos."""
    total_alunos = len(alunos)
    
    if total_alunos == 0:
        print("Nenhum aluno cadastrado.")
        time.sleep(10)  # Espera 10 segundos antes de retornar
        return
    
    print("\nLista de Alunos:")
    print("=" * 40)  # Linha de separação
    for matricula, nome in alunos.items():
        print(f"Matrícula: {matricula:<10} | Nome: {nome}")
    
    print("=" * 40)  # Linha de separação
    print(f"Total de alunos cadastrados: {total_alunos}")
    
    time.sleep(10)  # Espera 10 segundos antes de retornar