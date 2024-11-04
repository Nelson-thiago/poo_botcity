
class Livro:
    def __init__(self, codigo, titulo, autor=None, ano_publi=None, genero=None):
        #self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publi = ano_publi
        self.__genero = genero

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

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def ano_publi(self):
        return self.__ano_publi

    @ano_publi.setter
    def ano_publi(self, ano_publi):
        self.__ano_publi = ano_publi

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero


    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" já está emprestado.')

    def devolver(self):
        if not self.disponibilidade:
            self.disponibilidade = True
            print(f'O livro "{self.titulo}" foi devolvido.')
        else:
            print(f'O livro "{self.titulo}" já está disponível.')

    def mostrar_info(self):
        status = "disponível" if self.disponibilidade else "indisponível"
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {status}')


