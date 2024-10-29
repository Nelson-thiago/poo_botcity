class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome   # Armazena o nome em uma variável privada
        self._idade = idade # Armazena a idade em uma variável privada

    @property
    def idade(self):
        return self._idade  # Retorna a variável privada _idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("a idade nao pode ser negativa")
        self._idade = valor # Atribui o valor à variável privada _idade

    @property
    def nome(self):
        return self._nome   # Retorna a variável privada _nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("o nome nao pode ser vazio")
        self._nome = valor  # Atribui o valor à variável privada _nome

# Criando uma instância da classe
try:
    pessoa = Pessoa('alice', 30)
    print(pessoa.idade)  # Saída: 30
    pessoa.idade = -5    # Levantará um ValueError
    print(pessoa.idade)
except ValueError as e:
    print(e)

try:
    pessoa.nome = ""      # Levantará um ValueError
except ValueError as e:
    print(e)
