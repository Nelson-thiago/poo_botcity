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
    def calcular_Salario():
        pass

class funcionarioHorista(funcionario):
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
    
    def calcular_Salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        return salario


class funcionarioMensalista(funcionario):   
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self.__salario_mensal= salario_mensal

    @property
    def salario_mensal(self):
        return self.__salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, salario_mensal):
        self.__salario_mensal = salario_mensal

    def calcular_Salario(self):
        salario = self.salario_mensal
        return salario

class funcionarioComissionado(funcionario):
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

    def calcular_Salario(self):
        salario = self.salario_base + (self.vendas * self.taxa_comissao)
        return salario

def calcular_pagamento(funcionario):
    print(f"salario {funcionario.nome}: R${funcionario.calcular_Salario()}")

def testar_funcionarios():
    horista = funcionarioHorista(nome="João", matricula="001", horas_trabalhadas=160, valor_hora=50)
    
    mensalista = funcionarioMensalista(nome="Maria", matricula="002", salario_mensal=4000)
    
    comissionado = funcionarioComissionado(nome="Carlos", matricula="003", salario_base=2000, vendas=50000, taxa_comissao=0.1)

    funcionarios = [horista, mensalista, comissionado]

    for funcionario in funcionarios:
        calcular_pagamento(funcionario)

# Testar a função
testar_funcionarios()
