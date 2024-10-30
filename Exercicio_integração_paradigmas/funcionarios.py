import sys
sys.stdout.reconfigure(encoding='utf-8')

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario
        
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def __str__(self):
        return f"{self.nome} - {self.cargo} - Salário: {self.salario}"

class SistemaRH:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def autenticar_acesso(func):
        def wrapper(self, funcionario, *args, **kwargs):
            if funcionario.cargo == "Gerente":
                return func(self, funcionario, *args, **kwargs)
            else:
                print(f"Acesso negado para {funcionario.nome}. Apenas gerentes podem aumentar o salário.")
                return None
        return wrapper

    @autenticar_acesso
    def aumentar_salario(self, funcionario, aumento_percentual):
        for f in self.funcionarios:
            f.salario += f.salario * aumento_percentual / 100
            print(f"Salário de {f.nome} atualizado para: {f.salario}")


func1 = Funcionario("Alice", "Gerente", 5000)
func2 = Funcionario("Bob", "Analista", 3000)

sistema_rh = SistemaRH()
sistema_rh.adicionar_funcionario(func1)
sistema_rh.adicionar_funcionario(func2)

# É Gerente
sistema_rh.aumentar_salario(func1, 10)

# não é Gerente
sistema_rh.aumentar_salario(func2, 10)
