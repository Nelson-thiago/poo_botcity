import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.autor import Autor
from classes.livro import Livro
from classes.biblioteca import Biblioteca

# Inicializando biblioteca e objetos
biblioteca = Biblioteca("Biblioteca Central")
autor1 = Autor("001", "George Orwell")
livro1 = Livro("1984", "1984", autor1)
biblioteca.adicionar_livro(livro1)

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("500x450")

        # Seção para cadastrar novos livros
        self.lbl_titulo = tk.Label(root, text="Título do Livro")
        self.lbl_titulo.pack()
        self.entry_titulo = tk.Entry(root)
        self.entry_titulo.pack()

        self.lbl_codigo = tk.Label(root, text="Código do Livro")
        self.lbl_codigo.pack()
        self.entry_codigo = tk.Entry(root)
        self.entry_codigo.pack()

        self.btn_adicionar_livro = tk.Button(root, text="Adicionar Livro", command=self.adicionar_livro)
        self.btn_adicionar_livro.pack(pady=5)

        # Separador horizontal
        self.separator1 = ttk.Separator(root, orient='horizontal')
        self.separator1.pack(fill='x', pady=10)

        # Seção para ações de empréstimo
        self.lbl_emprestimo = tk.Label(root, text="Código do Livro para Empréstimo")
        self.lbl_emprestimo.pack()
        self.entry_emprestimo = tk.Entry(root)
        self.entry_emprestimo.pack()

        self.lbl_cliente = tk.Label(root, text="Nome do Cliente")
        self.lbl_cliente.pack()
        self.entry_cliente = tk.Entry(root)
        self.entry_cliente.pack()

        self.btn_emprestar = tk.Button(root, text="Emprestar Livro", command=self.emprestar_livro)
        self.btn_emprestar.pack(pady=5)

        # Separador horizontal
        self.separator2 = ttk.Separator(root, orient='horizontal')
        self.separator2.pack(fill='x', pady=10)

        # Seção para ações de devolução
        self.lbl_devolucao = tk.Label(root, text="Código do Livro para Devolução")
        self.lbl_devolucao.pack()
        self.entry_devolucao = tk.Entry(root)
        self.entry_devolucao.pack()

        self.btn_devolver = tk.Button(root, text="Devolver Livro", command=self.devolver_livro)
        self.btn_devolver.pack(pady=5)

        # Separador horizontal
        self.separator3 = ttk.Separator(root, orient='horizontal')
        self.separator3.pack(fill='x', pady=10)

        # Botão para listar livros disponíveis
        self.btn_listar_livros = tk.Button(root, text="Listar Livros Disponíveis", command=self.listar_livros)
        self.btn_listar_livros.pack(pady=10)

    def limpar_campos(self):
        # Limpa os campos de entrada
        self.entry_titulo.delete(0, tk.END)
        self.entry_codigo.delete(0, tk.END)
        self.entry_devolucao.delete(0, tk.END)
        self.entry_emprestimo.delete(0, tk.END)
        self.entry_cliente.delete(0, tk.END)

    def adicionar_livro(self):
        titulo = self.entry_titulo.get()
        codigo = self.entry_codigo.get()
        if titulo and codigo:
            livro = Livro(codigo, titulo)
            biblioteca.adicionar_livro(livro)
            messagebox.showinfo("Sucesso", f'Livro "{titulo}" adicionado com sucesso!')
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")
        self.limpar_campos()

    def emprestar_livro(self):
        codigo = self.entry_emprestimo.get()
        nome_cliente = self.entry_cliente.get()
        if codigo and nome_cliente:
            livro = biblioteca._buscar_livro_por_codigo(codigo)
            if livro and livro.disponibilidade:
                biblioteca.registrar_emprestimo(codigo, nome_cliente)
                messagebox.showinfo("Sucesso", f'Livro "{livro.titulo}" emprestado com sucesso para {nome_cliente}!')
            else:
                messagebox.showwarning("Erro", "Livro não disponível para empréstimo.")
            self.limpar_campos()
        else:
            messagebox.showwarning("Erro", "Preencha o código do livro e o nome do cliente.")
        self.limpar_campos()

    def devolver_livro(self):
        codigo = self.entry_devolucao.get()
        if codigo:
            livro = biblioteca._buscar_livro_por_codigo(codigo)
            if livro and not livro.disponibilidade:
                biblioteca.registrar_devolucao(codigo)
                messagebox.showinfo("Sucesso", f'Livro "{livro.titulo}" devolvido com sucesso!')
            else:
                messagebox.showwarning("Erro", "Livro não está emprestado.")
            self.limpar_campos()
        else:
            messagebox.showwarning("Erro", "Preencha o código do livro.")
        self.limpar_campos()

    def listar_livros(self):
        livros_disponiveis = [
            f"Código: {livro.codigo}, Título: {livro.titulo}, Disponibilidade: {'Disponível' if livro.disponibilidade else 'Indisponível'}"
            for livro in biblioteca._Biblioteca__livros
        ]
        if livros_disponiveis:
            livros_formatados = "\n".join(livros_disponiveis)
            messagebox.showinfo("Livros Disponíveis", livros_formatados)
        else:
            messagebox.showinfo("Livros Disponíveis", "Nenhum livro disponível.")

# Executando o app
root = tk.Tk()
app = BibliotecaApp(root)
root.mainloop()
