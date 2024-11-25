import tkinter as tk

def converter():
    try:
        # Obter o valor em centímetros do campo de entrada
        centimetros = float(entry_centimetros.get())

        # Converter para metros
        metros = centimetros / 100

        # Exibir o resultado
        label_resultado.config(text=f"{centimetros} cm são equivalentes a {metros} m.")

    except ValueError:
        label_resultado.config(text="Por favor, insira um valor numérico válido.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")

# Criar os elementos da interface
label_centimetros = tk.Label(janela, text="Digite o valor em centímetros:")
entry_centimetros = tk.Entry(janela)
botao_converter = tk.Button(janela, text="Converter", command=converter)
label_resultado = tk.Label(janela, text="")

# Posicionar os elementos na janela
label_centimetros.pack()
entry_centimetros.pack()
botao_converter.pack()
label_resultado.pack()

# Iniciar o loop principal da aplicação
janela.mainloop()