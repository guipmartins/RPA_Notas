import tkinter as tk
from tkinter import messagebox

def calcular_notas(valor_saque, limite_diario, limite_por_saque):
    if valor_saque <= limite_diario and valor_saque <= limite_por_saque:
        notas_disp = [200, 100, 50, 20, 10, 5, 2]
        resultado = {}
        for nota in notas_disp:
            quantidade_notas = valor_saque // nota
            if quantidade_notas > 0:
                resultado[nota] = quantidade_notas
                valor_saque = valor_saque % nota
        
        # Check for any remainder left (should be less than 2)
        if valor_saque == 1:
            messagebox.showwarning("Nota Indisponível", "A nota de R$1,00 não está disponível. A nota mínima é R$2,00.")
            return None
        
        return resultado
    else:
        messagebox.showerror("Erro", "O valor de saque informado excede o limite diário ou limite por saque. Por favor, informe um novo valor.")
        return None

def processar_saque():
    valor_saque = int(valor_saque_entry.get())
    notas = calcular_notas(valor_saque, limite_diario, limite_por_saque)

    if notas:
        mensagem = "Notas a serem entregues:\n"
        for nota, quantidade in notas.items():
            mensagem += f"{quantidade} nota(s) de R${nota},00\n"
        messagebox.showinfo("Resultado do Saque", mensagem)

# Configurações da janela principal
janela = tk.Tk()
janela.title("Caixa Eletrônico")
janela.geometry("300x200")

# Labels e campos de entrada
valor_saque_label = tk.Label(janela, text="Digite o valor que você deseja sacar:")
valor_saque_label.pack()

valor_saque_entry = tk.Entry(janela)
valor_saque_entry.pack()

# Botão para processar o saque
processar_button = tk.Button(janela, text="Processar Saque", command=processar_saque)
processar_button.pack()

# Defina aqui o limite diário de saque e o limite por saque
limite_diario = 10000
limite_por_saque = 2000

# Inicia a execução da interface
janela.mainloop()
