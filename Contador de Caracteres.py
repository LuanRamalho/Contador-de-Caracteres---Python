import tkinter as tk

def contar_caracteres():
    texto = texto_input.get("1.0", "end-1c")  # Obtém o texto da caixa de texto
    caracteres_com_espacos = len(texto)
    caracteres_sem_espacos = len(texto.replace(" ", ""))
    
    resultado_label.config(text=f"Caracteres com espaço: {caracteres_com_espacos}\n"
                                 f"Caracteres sem espaço: {caracteres_sem_espacos}")

# Cria a janela principal
janela = tk.Tk()
janela.title("Contador de Caracteres")
janela.geometry("500x400")
janela.config(bg="#f0f8ff")  # Cor de fundo suave

# Cria uma caixa de texto para o usuário inserir texto
texto_input = tk.Text(janela, height=10, width=50, font=("Arial", 12), bg="#ffffff", fg="#333333", bd=2, relief="solid")
texto_input.pack(pady=20)

# Cria um botão para contar caracteres
contar_button = tk.Button(janela, text="Contar Caracteres", command=contar_caracteres, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", bd=0, relief="raised")
contar_button.pack(pady=10)

# Label para exibir os resultados
resultado_label = tk.Label(janela, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
resultado_label.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
