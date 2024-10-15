class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" já está emprestado.')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'O livro "{self.titulo}" foi devolvido.')
        else:
            print(f'O livro "{self.titulo}" já está disponível.')

    def mostrar_info(self):
        status = "disponível" if self.disponivel else "indisponível"
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {status}')


# Exemplo de uso

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
