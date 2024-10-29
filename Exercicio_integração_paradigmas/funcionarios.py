import sys
sys.stdout.reconfigure(encoding='utf-8')

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

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

# Exemplo de uso
func1 = Funcionario("Alice", "Gerente", 5000)
func2 = Funcionario("Bob", "Analista", 3000)

sistema_rh = SistemaRH()
sistema_rh.adicionar_funcionario(func1)
sistema_rh.adicionar_funcionario(func2)

# Aumento permitido (Gerente)
sistema_rh.aumentar_salario(func1, 10)

# Aumento negado (não é Gerente)
sistema_rh.aumentar_salario(func2, 10)
