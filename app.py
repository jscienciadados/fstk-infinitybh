import tkinter as tk

def verificar_login():
    email = email_entry.get()
    senha = senha_entry.get()

    if len(senha) < 6:
        resultado_label.config(text="A senha deve ter no mínimo 6 caracteres.")
    elif "@" not in email:
        resultado_label.config(text="O email deve conter o símbolo @.")
    else:
        resultado_label.config(text="Login realizado com sucesso!")

# Criando a janela principal
root = tk.Tk()
root.title("Tela de Login")

# Criando os labels e campos de entrada
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

senha_label = tk.Label(root, text="Senha:")
senha_label.pack()
senha_entry = tk.Entry(root, show="*")  # Mostra asteriscos no lugar da senha
senha_entry.pack()

# Botão para verificar o login
login_button = tk.Button(root, text="Login", command=verificar_login)
login_button.pack()

# Label para exibir o resultado da verificação
resultado_label = tk.Label(root, text="")
resultado_label.pack()

root.mainloop()