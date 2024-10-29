import sys
import os
import tkinter as tk
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

class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []
        self.__emprestimos = {}

    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.__livros.append(livro)
        else:
            raise ValueError("O objeto fornecido não é uma instância da classe Livro.")

    def registrar_emprestimo(self, codigo_livro):
        livro = self._buscar_livro_por_codigo(codigo_livro)
        if livro and livro.disponibilidade:
            livro.emprestar()
            self.__emprestimos[codigo_livro] = "Cliente"
        else:
            print(f'O livro com código {codigo_livro} não está disponível para empréstimo.')

    def registrar_devolucao(self, codigo_livro):
        livro = self._buscar_livro_por_codigo(codigo_livro)
        if livro and not livro.disponibilidade:
            livro.devolver()
            del self.__emprestimos[codigo_livro]
        else:
            print(f'O livro com código {codigo_livro} não está emprestado.')

    def _buscar_livro_por_codigo(self, codigo_livro):
        for livro in self.__livros:
            if livro.codigo == codigo_livro:
                return livro
        return None


# Inicializando biblioteca e objetos
biblioteca = Biblioteca("Biblioteca Central")
autor1 = Autor("001", "George Orwell")
livro1 = Livro("1984", "1984", autor1)
biblioteca.adicionar_livro(livro1)


# Interface Tkinter
class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("500x400")

        # Campo para cadastrar novos livros
        self.lbl_titulo = tk.Label(root, text="Título do Livro")
        self.lbl_titulo.pack()
        self.entry_titulo = tk.Entry(root)
        self.entry_titulo.pack()

        self.lbl_codigo = tk.Label(root, text="Código do Livro")
        self.lbl_codigo.pack()
        self.entry_codigo = tk.Entry(root)
        self.entry_codigo.pack()

        self.btn_adicionar_livro = tk.Button(root, text="Adicionar Livro", command=self.adicionar_livro)
        self.btn_adicionar_livro.pack()

        # Botões de ações para empréstimo e devolução
        self.lbl_emprestimo = tk.Label(root, text="Código do Livro para Empréstimo")
        self.lbl_emprestimo.pack()
        self.entry_emprestimo = tk.Entry(root)
        self.entry_emprestimo.pack()

        self.btn_emprestar = tk.Button(root, text="Emprestar Livro", command=self.emprestar_livro)
        self.btn_emprestar.pack()

        self.lbl_devolucao = tk.Label(root, text="Código do Livro para Devolução")
        self.lbl_devolucao.pack()
        self.entry_devolucao = tk.Entry(root)
        self.entry_devolucao.pack()

        self.btn_devolver = tk.Button(root, text="Devolver Livro", command=self.devolver_livro)
        self.btn_devolver.pack()

        # Botão para listar livros disponíveis
        self.btn_listar_livros = tk.Button(root, text="Listar Livros Disponíveis", command=self.listar_livros)
        self.btn_listar_livros.pack()

    def adicionar_livro(self):
        titulo = self.entry_titulo.get()
        codigo = self.entry_codigo.get()
        if titulo and codigo:
            livro = Livro(codigo, titulo)
            biblioteca.adicionar_livro(livro)
            messagebox.showinfo("Sucesso", f'Livro "{titulo}" adicionado com sucesso!')
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def emprestar_livro(self):
        codigo = self.entry_emprestimo.get()
        if codigo:
            livro = biblioteca._buscar_livro_por_codigo(codigo)
            if livro and livro.disponibilidade:
                biblioteca.registrar_emprestimo(codigo)
                messagebox.showinfo("Sucesso", f'Livro "{livro.titulo}" emprestado com sucesso!')
            else:
                messagebox.showwarning("Erro", "Livro não disponível para empréstimo.")
        else:
            messagebox.showwarning("Erro", "Preencha o código do livro.")

    def devolver_livro(self):
        codigo = self.entry_devolucao.get()
        if codigo:
            livro = biblioteca._buscar_livro_por_codigo(codigo)
            if livro and not livro.disponibilidade:
                biblioteca.registrar_devolucao(codigo)
                messagebox.showinfo("Sucesso", f'Livro "{livro.titulo}" devolvido com sucesso!')
            else:
                messagebox.showwarning("Erro", "Livro não está emprestado.")
        else:
            messagebox.showwarning("Erro", "Preencha o código do livro.")

    def listar_livros(self):
        livros_disponiveis = [livro.titulo for livro in biblioteca._Biblioteca__livros if livro.disponibilidade]
        if livros_disponiveis:
            messagebox.showinfo("Livros Disponíveis", "\n".join(livros_disponiveis))
        else:
            messagebox.showinfo("Livros Disponíveis", "Nenhum livro disponível.")

# Executando o app
root = tk.Tk()
app = BibliotecaApp(root)
root.mainloop()
