import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campos do formulário
    name_field = ft.TextField(label="Nome Completo", width=300)
    email_field = ft.TextField(label="Email", keyboard_type=ft.KeyboardType.EMAIL, width=300)
    message_field = ft.TextField(label="Mensagem", multiline=True, min_lines=3, max_lines=5, width=300)

    # Mensagem de confirmação
    confirmation_message = ft.Text("", visible=False, color=ft.Colors.GREEN_600) # ERRO CORRIGIDO AQUI!

    def send_form(e):
        # Processar os dados (aqui, apenas exibimos uma confirmação)
        print(f"Nome: {name_field.value}")
        print(f"Email: {email_field.value}")
        print(f"Mensagem: {message_field.value}")

        confirmation_message.value = "Formulário enviado com sucesso!"
        confirmation_message.visible = True
        page.update()

        # Limpar os campos após o envio (opcional)
        name_field.value = ""
        email_field.value = ""
        message_field.value = ""
        page.update()

    # Botão de envio
    submit_button = ft.ElevatedButton("Enviar", on_click=send_form)

    page.add(
        ft.Column(
            [
                ft.Text("Formulário de Contato", size=24, weight=ft.FontWeight.BOLD),
                name_field,
                email_field,
                message_field,
                submit_button,
                confirmation_message,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10, # Espaçamento entre os componentes da coluna
        )
    )

if __name__ == "__main__":
    ft.app(target=main)