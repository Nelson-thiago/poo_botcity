from livro import Livro 
from autor import Autor
from biblioteca import Biblioteca

# Testando o sistema da biblioteca

# Criando autores
print("\n================================")
autor1 = Autor(1, "George Orwell")
autor2 = Autor(2, "J.R.R. Tolkien")

# Criando livros e associando aos autores
print("\n================================")
livro1 = Livro(1, "1984", autor1)
livro2 = Livro(2, "O Senhor dos Anéis", autor2)
livro3 = Livro(3, "A Revolução dos Bichos", autor1)
# Adicionando livros aos autores

print("\n================================")
autor1.adicionar_livro(livro1)
autor1.adicionar_livro(livro3)
autor2.adicionar_livro(livro2)

# Exibindo os livros dos autores
print("\n================================")
autor1.mostrar_livros()
autor2.mostrar_livros()

# Criando a biblioteca
print("\n================================")
biblioteca = Biblioteca("Biblioteca Central")

# Adicionando livros à biblioteca
print("\n================================")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Exibindo o total de livros na biblioteca
print("\n================================")
Biblioteca.mostrar_total_livros()

# Mostrando livros disponíveis para empréstimo
print("\n================================")
biblioteca.mostrar_livros_disponiveis()

# Registrando empréstimo
print("\n================================")
print("\nRealizando empréstimo do livro '1984'...")
biblioteca.registrar_emprestimo(1, "Cliente A")

# Tentando emprestar o mesmo livro novamente
print("\n================================")
print("\nTentando emprestar o livro '1984' novamente...")
biblioteca.registrar_emprestimo(1, "Cliente B")

# Exibindo livros disponíveis após o empréstimo
print("\n================================")
print("\nLivros disponíveis após o empréstimo:")
biblioteca.mostrar_livros_disponiveis()

# Registrando devolução
print("\n================================")
print("\nDevolvendo o livro '1984'...")
biblioteca.registrar_devolucao(1)

# Mostrando livros disponíveis após a devolução
print("\n================================")
print("\nLivros disponíveis após a devolução:")
biblioteca.mostrar_livros_disponiveis()

# Tentando devolver um livro que já está disponível
print("\n================================")
print("\nTentando devolver o livro '1984' novamente...")
biblioteca.registrar_devolucao(1)
