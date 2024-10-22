import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora

    def calcular_salario(self):
        return self.__horas_trabalhadas * self.__valor_hora

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self.__salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.__salario_mensal

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self.__salario_base = salario_base
        self.__vendas = vendas
        self.__taxa_comissao = taxa_comissao

    def calcular_salario(self):
        return self.__salario_base + (self.__vendas * self.__taxa_comissao)


class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora

    def calcular_salario(self):
        return self.__horas_trabalhadas * self.__valor_hora

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self.__salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.__salario_mensal

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self.__salario_base = salario_base
        self.__vendas = vendas
        self.__taxa_comissao = taxa_comissao

    def calcular_salario(self):
        return self.__salario_base + (self.__vendas * self.__taxa_comissao)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Funcionários")
        self.funcionarios = []  # Lista para armazenar os funcionários
        self.create_widgets()

    def create_widgets(self):
        self.label_nome = ttk.Label(self.root, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = ttk.Entry(self.root)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_matricula = ttk.Label(self.root, text="Matrícula:")
        self.label_matricula.grid(row=1, column=0, padx=5, pady=5)
        self.entry_matricula = ttk.Entry(self.root)
        self.entry_matricula.grid(row=1, column=1, padx=5, pady=5)

        self.label_tipo = ttk.Label(self.root, text="Tipo de Funcionário:")
        self.label_tipo.grid(row=2, column=0, padx=5, pady=5)
        self.tipo_funcionario = ttk.Combobox(self.root, values=["Horista", "Mensalista", "Comissionado"])
        self.tipo_funcionario.grid(row=2, column=1, padx=5, pady=5)
        self.tipo_funcionario.bind("<<ComboboxSelected>>", self.update_fields)

        self.button_registrar = ttk.Button(self.root, text="Registrar Funcionário", command=self.registrar_funcionario)
        self.button_registrar.grid(row=6, column=0, columnspan=2, pady=10)

        self.button_listar = ttk.Button(self.root, text="Listar Funcionários", command=self.abrir_lista)
        self.button_listar.grid(row=7, column=0, columnspan=2, pady=10)

        self.label_resultado = ttk.Label(self.root, text="Salário:")
        self.label_resultado.grid(row=8, column=0, padx=5, pady=5)
        self.resultado = ttk.Label(self.root, text="")
        self.resultado.grid(row=8, column=1, padx=5, pady=5)

        self.dynamic_fields = {}

    def update_fields(self, event):
        for widget in self.dynamic_fields.values():
            widget.destroy()
        self.dynamic_fields.clear()

        tipo = self.tipo_funcionario.get()
        if tipo == "Horista":
            self.add_dynamic_field("horas_trabalhadas", "Horas Trabalhadas:")
            self.add_dynamic_field("valor_hora", "Valor Hora:")
        elif tipo == "Mensalista":
            self.add_dynamic_field("salario_mensal", "Salário Mensal:")
        elif tipo == "Comissionado":
            self.add_dynamic_field("salario_base", "Salário Base:")
            self.add_dynamic_field("vendas", "Vendas:")
            self.add_dynamic_field("taxa_comissao", "Taxa Comissão:")

    def add_dynamic_field(self, key, label_text):
        label = ttk.Label(self.root, text=label_text)
        label.grid(row=len(self.dynamic_fields) + 3, column=0, padx=5, pady=5)
        entry = ttk.Entry(self.root)
        entry.grid(row=len(self.dynamic_fields) + 3, column=1, padx=5, pady=5)
        self.dynamic_fields[key] = entry

    def registrar_funcionario(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        tipo = self.tipo_funcionario.get()

        if tipo == "Horista":
            horas_trabalhadas = float(self.dynamic_fields["horas_trabalhadas"].get())
            valor_hora = float(self.dynamic_fields["valor_hora"].get())
            funcionario = FuncionarioHorista(nome, matricula, horas_trabalhadas, valor_hora)

        elif tipo == "Mensalista":
            salario_mensal = float(self.dynamic_fields["salario_mensal"].get())
            funcionario = FuncionarioMensalista(nome, matricula, salario_mensal)

        elif tipo == "Comissionado":
            salario_base = float(self.dynamic_fields["salario_base"].get())
            vendas = float(self.dynamic_fields["vendas"].get())
            taxa_comissao = float(self.dynamic_fields["taxa_comissao"].get())
            funcionario = FuncionarioComissionado(nome, matricula, salario_base, vendas, taxa_comissao)

        # Exibir os dados do funcionário cadastrados
        messagebox.showinfo("Cadastro de Funcionário", f'Funcionário Cadastrado:\nNome: {funcionario.nome}\nMatrícula: {funcionario.matricula}\nTipo: {tipo}\nSalário: R${funcionario.calcular_salario():.2f}')

        self.funcionarios.append(funcionario)  # Adiciona funcionário à lista
        salario = funcionario.calcular_salario()
        self.resultado.config(text=f"R${salario:.2f}")

    def abrir_lista(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Funcionários Cadastrados")

        # Criação do Treeview com colunas para Nome, Matrícula, Tipo e Salário
        tree = ttk.Treeview(nova_janela, columns=("Nome", "Matricula", "Tipo", "Salario"), show='headings')
        tree.heading("Nome", text="Nome")
        tree.heading("Matricula", text="Matrícula")
        tree.heading("Tipo", text="Tipo")
        tree.heading("Salario", text="Salário (R$)")
        
        # Definindo a largura das colunas
        tree.column("Nome", width=150)
        tree.column("Matricula", width=100)
        tree.column("Tipo", width=100)
        tree.column("Salario", width=100)
        
        # Adiciona os funcionários na tabela
        for funcionario in self.funcionarios:
            tipo = "Horista" if isinstance(funcionario, FuncionarioHorista) else \
                "Mensalista" if isinstance(funcionario, FuncionarioMensalista) else \
                "Comissionado"
            tree.insert("", "end", values=(funcionario.nome, funcionario.matricula, tipo, f"R${funcionario.calcular_salario():.2f}"))
        
        # Adiciona a scrollbar
        scrollbar = ttk.Scrollbar(nova_janela, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)

        # Posiciona o Treeview e a scrollbar
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
