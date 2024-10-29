import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

from abc import ABC,abstractmethod

class funcionario(ABC):
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @abstractmethod
    def calcular_salario():
        pass

class FuncionarioHorista(funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora

    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, horas_trabalhadas):
        self.__horas_trabalhadas = horas_trabalhadas
    
    @property
    def valor_hora(self):
        return self.__valor_hora

    @valor_hora.setter
    def valor_hora(self, valor_hora):
        self.__valor_hora = valor_hora
    
    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        return salario


class FuncionarioMensalista(funcionario):   
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self.__salario_mensal= salario_mensal

    @property
    def salario_mensal(self):
        return self.__salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, salario_mensal):
        self.__salario_mensal = salario_mensal

    def calcular_salario(self):
        salario = self.salario_mensal
        return salario

class FuncionarioComissionado(funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self.__salario_base = salario_base
        self.__vendas = vendas
        self.__taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

    @property
    def vendas(self):
        return self.__vendas

    @vendas.setter
    def vendas(self, vendas):
        self.__vendas = vendas

    @property
    def taxa_comissao(self):
        return self.__taxa_comissao

    @taxa_comissao.setter
    def taxa_comissao(self, taxa_comissao):
        self.__taxa_comissao = taxa_comissao

    def calcular_salario(self):
        salario = self.salario_base + (self.vendas * self.taxa_comissao)
        return salario


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

        # Campo de salario

        # self.label_resultado = ttk.Label(self.root, text="Salário:")
        # self.label_resultado.grid(row=8, column=0, padx=5, pady=5)
        # self.resultado = ttk.Label(self.root, text="")
        # self.resultado.grid(row=8, column=1, padx=5, pady=5)

        self.dynamic_fields = {}

    def update_fields(self, event):
        # Remove campos dinâmicos antigos antes de criar novos
        for widget in self.dynamic_fields.values():
            widget[0].destroy()  # Destrói o Label
            widget[1].destroy()  # Destrói o Entry
        self.dynamic_fields.clear()

        # Define os campos dinâmicos de acordo com o tipo de funcionário selecionado
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
        self.dynamic_fields[key] = (label, entry)  # Armazena o par (label, entry)

    def registrar_funcionario(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        tipo = self.tipo_funcionario.get()

        try:
            if tipo == "Horista":
                horas_trabalhadas = float(self.dynamic_fields["horas_trabalhadas"][1].get())
                valor_hora = float(self.dynamic_fields["valor_hora"][1].get())
                funcionario = FuncionarioHorista(nome, matricula, horas_trabalhadas, valor_hora)
            elif tipo == "Mensalista":
                salario_mensal = float(self.dynamic_fields["salario_mensal"][1].get())
                funcionario = FuncionarioMensalista(nome, matricula, salario_mensal)
            elif tipo == "Comissionado":
                salario_base = float(self.dynamic_fields["salario_base"][1].get())
                vendas = float(self.dynamic_fields["vendas"][1].get())
                taxa_comissao = float(self.dynamic_fields["taxa_comissao"][1].get())
                funcionario = FuncionarioComissionado(nome, matricula, salario_base, vendas, taxa_comissao)
            else:
                raise ValueError("Tipo de funcionário inválido.")

            messagebox.showinfo("Cadastro de Funcionário", f'Funcionário Cadastrado:\nNome: {funcionario.nome}\nMatrícula: {funcionario.matricula}\nTipo: {tipo}\nSalário: R${funcionario.calcular_salario():.2f}')
            self.funcionarios.append(funcionario)
            salario = funcionario.calcular_salario()
#            self.resultado.config(text=f"R${salario:.2f}")

        except ValueError as e:
            messagebox.showerror("Erro de Cadastro", f"Erro ao cadastrar funcionário: {e}")

    def abrir_lista(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Funcionários Cadastrados")

        tree = ttk.Treeview(nova_janela, columns=("Nome", "Matricula", "Tipo", "Salario"), show='headings')
        tree.heading("Nome", text="Nome")
        tree.heading("Matricula", text="Matrícula")
        tree.heading("Tipo", text="Tipo")
        tree.heading("Salario", text="Salário (R$)")
        
        tree.column("Nome", width=150)
        tree.column("Matricula", width=100)
        tree.column("Tipo", width=100)
        tree.column("Salario", width=100)
        
        for i, funcionario in enumerate(self.funcionarios):
            tipo = "Horista" if isinstance(funcionario, FuncionarioHorista) else \
                "Mensalista" if isinstance(funcionario, FuncionarioMensalista) else \
                "Comissionado"
            tree.insert("", "end", iid=i, values=(funcionario.nome, funcionario.matricula, tipo, f"R${funcionario.calcular_salario():.2f}"))

        tree.pack(side="left", fill="both", expand=True)

        button_delete = ttk.Button(nova_janela, text="Apagar Funcionário", command=lambda: self.apagar_funcionario(tree))
        button_delete.pack(pady=10)

    def apagar_funcionario(self, tree):
        selected_item = tree.selection()
        if selected_item:
            index = int(selected_item[0])  # Pega o índice do item selecionado
            del self.funcionarios[index]   # Remove da lista de funcionários
            tree.delete(selected_item)     # Remove da Treeview
            messagebox.showinfo("Funcionário Removido", "Funcionário apagado com sucesso.")
        else:
            messagebox.showwarning("Seleção Inválida", "Selecione um funcionário para apagar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()