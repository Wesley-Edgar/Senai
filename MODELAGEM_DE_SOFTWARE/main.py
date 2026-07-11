import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF

def gerar_pdf():
    cliente = entrada_cliente.get()
    servico = combo_servi vco.get()
    valor = entrada_valor.get()

       #Validação de campos
    if not cliente or not servico or not valor :
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    try:
        pdf = FPDF()
        pdf.add_page() #Adicionar página
        pdf.set_font('arial', size = 12)
        pdf.cell(200, 10, txt = "ORDEM DE SERVIÇO", ln= 1, align = "C")

        pdf.ln(10)
        pdf.cell(200, 10, txt = f"Cliente: {cliente}", ln=1)
        pdf.cell(200, 10, txt = f"Serviço: {servico}", ln=1)
        pdf.cell(200, 10, txt = f"Valor: {valor}", ln=1)

        pdf.output("ordem_de_servico.pdf")
        messagebox.showinfo ("Sucesso", "PDF gerado com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar o PDF: {e}")

# Criação da interface Gráfica (Tkinter)
janela = tk.Tk()
janela.title("Gerador de Ordem de Serviço")
janela.geometry("300x300")

tk.Label(janela, text = "Cliente").grid(
    row = 0,
    column = 0,
    padx = 10,
    sticky = "w",
    pady = 5
)
entrada_cliente = tk.Entry(janela, width = 28)
entrada_cliente.grid(row=0, column = 1, padx = 10, pady = 5)

# COMBOBOX SERVICO
servicos = [
    "Formatação de computador",
    "Instalação de Windows",
    "Manutenção de rede",
    "Criação de site",
    "Suporte técnico"
]
tk.Label(janela, text = "Serviço").grid(
    row = 2,
    column = 0,
    padx = 10,
    sticky = "w",
    pady = 5
)
combo_servico = ttk.Combobox(janela, values = servicos , width = 28)
combo_servico.grid(row=2, column = 1, padx = 10, pady = 5)

tk.Label(janela, text = "Valor").grid(
    row = 4,
    column = 0,
    padx = 10,
    sticky = "w",
    pady = 5
)
entrada_valor = tk.Entry(janela, width = 28)
entrada_valor.grid(row=4, column = 1, padx = 10, pady = 5)

# BOTÃO: GERAR PDF
botao_pdf = tk.Button(janela, text = "PDF", command = gerar_pdf, bg = "Green", fg = "white")
botao_pdf.grid(row = 6, column = 1, padx = 10, pady = 5)
janela.mainloop()