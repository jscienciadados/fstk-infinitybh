import flet as ft

def main(page: ft.Page):
    # Configuração inicial da página
    page.title = "Lista de Tarefas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Campo de entrada para nova tarefa
    new_task = ft.TextField(
        hint_text="Digite uma nova tarefa...",
        width=300,
        on_submit=lambda e: add_task(e, new_task, tasks_view, table, page)
    )
    
    # Botão para adicionar tarefa
    def add_task(e, field, tasks_view, table, page):
        if field.value.strip():
            tasks_view.controls.append(
                ft.Checkbox(label=field.value)
            )
            table.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(value=field.value, expand=True),
                        ft.ElevatedButton(
                            text="Listar",
                            on_click=lambda e: show_task_details(field.value)
                        )
                    ]
                )
            )
            field.value = ""
            page.update()
    
    # Container para as tarefas
    tasks_view = ft.Column()
    
    # Container para a tabela
    table = ft.Column(
        width=600,
        visible=False
    )
    
    # Função para mostrar detalhes da tarefa
    def show_task_details(task_name):
        page.controls.append(
            ft.AlertDialog(
                title=ft.Text(f"Detalhes da Tarefa: {task_name}"),
                content=ft.Text(f"Tarefa: {task_name}\nStatus: Pendente"),
                actions=[
                    ft.TextButton("Fechar", on_click=lambda e: page.controls.pop())
                ]
            )
        )
        page.update()
    
    # Botão para mostrar/ocultar tabela
    def toggle_table(e):
        table.visible = not table.visible
        toggle_btn.text = "Mostrar Tabela" if not table.visible else "Ocultar Tabela"
        page.update()
    
    # Botão para alternar visibilidade da tabela
    toggle_btn = ft.ElevatedButton(
        text="Mostrar Tabela",
        on_click=toggle_table
    )
    
    # Layout principal
    page.add(
        ft.Row(
            controls=[
                new_task,
                ft.ElevatedButton(
                    text="Adicionar",
                    on_click=lambda e: add_task(None, new_task, tasks_view, table, page)
                )
            ]
        ),
        tasks_view,
        toggle_btn,
        table
    )

ft.app(target=main)