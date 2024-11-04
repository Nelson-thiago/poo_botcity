import json
import csv
import pickle
from livro import Livro
from faker import Faker
import random
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

class Biblioteca:
    total_livros = 0
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []
        #self.__emprestimos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def livros(self):
        return self.__livros

    @livros.setter
    def livros(self, livros):
        self.__livros = livros


    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.__livros.append(livro)
            Biblioteca.total_livros += 1
            print(f'O livro "{livro.titulo}" foi adicionado à biblioteca "{self.nome}".')
        else:
            raise ValueError("O objeto fornecido não é uma instância da classe Livro.")

    def listar_livros_autor(self,autor):
        livros_autor = list(filter(lambda livro: livro.autor == autor, self.livros))
        if livros_autor:
            print(f"\nEncontrados {len(livros_autor)} livros do autor: {autor}")
            for livro in livros_autor:
                print(f'Titulo: {livro.titulo}, Ano: {livro.ano_publi}, Genero: {livro.genero}')
        else:
            print(f'Autor {autor} não encontrado.')

    def contar_livros_genero(self,genero):
        livros_genero = list(filter(lambda livro: livro.genero == genero, self.livros))
        if livros_genero:
            print(f"\nForam encontrados {len(livros_genero)} livros do genero: {genero}")
            for livro in livros_genero:
                print(f'Titulo: {livro.titulo}, autor: {livro.autor}, Ano: {livro.ano_publi}, Genero: {livro.genero}')
        else:
            print(f'\nNenhum livro do genero {genero} encontrado.')

    def salvar_dados(self, formato):
        if formato == 'csv':
            self.salvar_csv()
        elif formato == 'json':
            self.salvar_json()
        elif formato == 'pickle':
            self.salvar_pickle()
        else:
            print('Formato inválido')

#funçoes para salvar dados
    def salvar_json(self, nome_arquivo="livros.json"):
        dados = [{'Titulo': livro.titulo, 'Autor': livro.autor, 'Ano': livro.ano_publi, 'Genero': livro.genero} for livro in self.livros]
        with open(nome_arquivo, "w", encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        print(f"Dados salvos em {nome_arquivo}.")

    def salvar_csv(self, nome_arquivo="livros.csv"):
        with open(nome_arquivo, "w", newline="", encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Titulo", "Autor", "Ano", "Genero"])
            for livro in self.livros:
                escritor.writerow([livro.titulo, livro.autor, livro.ano_publi, livro.genero])
        print(f"Dados salvos em {nome_arquivo}.")

    def salvar_pickle(self, nome_arquivo="livros.pkl"):
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.livros, arquivo)
        print(f"Dados salvos em {nome_arquivo}.")

    def carregar_dados(self, formato):
        if formato == 'csv':
            self.carregar_csv()
        elif formato == 'json':
            self.carregar_json()
        elif formato == 'pickle':
            self.carregar_pickle()
        else:
            print('Formato inválido')

#funçoes para carregar dados
    def carregar_json(self, nome_arquivo="livros.json"):
        with open(nome_arquivo, "r") as arquivo_json:
            dados = json.load(arquivo_json)
            self.livros = [Livro(**livro) for livro in dados]
        print(f"Dados carregados de {nome_arquivo}.")

    def carregar_csv(self, nome_arquivo="livros.csv"):
        with open(nome_arquivo, "r",encoding="utf-8") as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            next(leitor)  # Pular cabeçalho
            self.livros = [Livro(linha[0], linha[1], int(linha[2]), linha[3]) for linha in leitor]  # Corrigido para evitar eval
        print(f"Dados carregados de {nome_arquivo}.")

    def carregar_pickle(self, nome_arquivo="livros.pkl"):
        with open(nome_arquivo, "rb") as arquivo:
            self.livros = pickle.load(arquivo)
        print(f"Dados carregados de {nome_arquivo}.")







def testar_biblioteca():

    fake = Faker()
    def gerar_livros(n):
        generos = ["Ficção", "Não-ficção", "Fantasia", "Romance", "Aventura", "Biografia", "Terror", "Mistério"]
        autores = ['Autor A', 'Autor B', 'Autor C', 'Autor D', 'Autor E', 'Autor F', 'Autor G', 'Autor H', 'Autor I', 'Autor J']
        livros = []

        for i in range(n):
            livro = {
                "codigo": f"LIVRO-{i+1:03}",  # Gera um código no formato LIVRO-001, LIVRO-002, etc.
                "titulo": fake.catch_phrase(),  # Gera um título fictício
                "autor": random.choice(autores),  # Gera um nome fictício de autor
                "ano_publi": random.randint(1900, 2024),  # Gera um ano de publicação aleatório
                "genero": random.choice(generos)  # Escolhe um gênero aleatório da lista
            }
            livros.append(livro)
        
        return livros

    n = 30  # Quantidade de livros a serem gerados
    livros_gerados = gerar_livros(n)

    biblioteca = Biblioteca('gnuteca')


    for livro_dicionario in livros_gerados:
        # Passar os valores do dicionário como argumentos para a classe Livro
        biblioteca.adicionar_livro(Livro(
            codigo=livro_dicionario["codigo"],
            titulo=livro_dicionario["titulo"],
            autor=livro_dicionario["autor"],
            ano_publi=livro_dicionario["ano_publi"],
            genero=livro_dicionario["genero"]
        )) 

    # Salvar dados em CSV
    biblioteca.salvar_dados('csv')

    # Limpar a lista de livros
    biblioteca.livros.clear()

    # Carregar os dados do CSV
    biblioteca.carregar_dados('csv')

    # Verificar se os dados carregados estão corretos
    for livro in biblioteca.livros:
        print(f'Titulo: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publi}, Genero: {livro.genero}')

    # Verificação
    assert len(biblioteca.livros) == len(livros_testes), "Número de livros carregados não coincide com o número de livros testados."
    for i, livro in enumerate(biblioteca.livros):
        assert livro.titulo == livros_testes[i].titulo, f'Título do livro {i} não confere.'
        assert livro.autor == livros_testes[i].autor, f'Autor do livro {i} não confere.'
        assert livro.ano_publi == livros_testes[i].ano_publi, f'Ano do livro {i} não confere.'
        assert livro.genero == livros_testes[i].genero, f'Gênero do livro {i} não confere.'
    
    print("Todos os testes passaram com sucesso!")

# Executar o teste
testar_biblioteca()