#Pouco armazenamento … 13% restantes do seu armazenamento individual de 1 GB. Para evitar interrupções, libere espaço ou fale com seu administrador.
import json
import csv
import pickle

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

class GerenciadorDeAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)



    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Média: {aluno.calcular_media():.2f}")

# Criando instância do gerenciador e adicionando alunos
gerenciador = GerenciadorDeAlunos()
gerenciador.adicionar_aluno(Aluno("Alice", 20, [8, 7.5, 9]))
gerenciador.adicionar_aluno(Aluno("Bob", 22, [6, 5, 7]))

# Salvando e carregando dados em JSON
gerenciador.salvar_json()
gerenciador.carregar_json()
gerenciador.listar_alunos()

# Salvando e carregando dados em CSV
gerenciador.salvar_csv()
gerenciador.carregar_csv()
gerenciador.listar_alunos()

# Salvando e carregando dados com pickle
gerenciador.salvar_pickle()
gerenciador.carregar_pickle()
gerenciador.listar_alunos()