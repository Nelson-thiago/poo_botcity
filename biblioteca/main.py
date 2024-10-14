# main.py
from livraria import Livraria  # Importando a classe Livraria
from livro import Livro  # Importando a classe Livro

# Exemplo de uso

livro1 = Livro("A Revolução dos Bichos", "George Orwell")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livraria = Livraria()

livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

livraria.mostrar_inventario()

livraria.emprestar_livro("A Revolução dos Bichos")
livraria.emprestar_livro("O Senhor dos Anéis")

livraria.mostrar_inventario()

livro1.devolver()
livraria.mostrar_inventario()
