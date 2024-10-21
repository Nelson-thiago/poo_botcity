from autor import Autor
class Livro:
    def __init__(self,codigo, titulo, autor=None, disponibilidade=True):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor.nome
        self.__disponibilidade = disponibilidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def autor(self):
        return self.__autor

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade



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
