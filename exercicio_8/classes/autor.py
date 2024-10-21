from livro import Livro 
class Autor:
    def __init__(self, codigo, nome, livros=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__livros = livros if livros is not None else []

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
    def livros(self):
        return self.__livros
    
    def adicionar_livro(self, livro):
        if isinstance(livro, livro):
            self.livros.append(livro)
            nome_livro = livro.nome

            print(f"livro {nome_livro} adicionado com sucesso")
        else:
            ValueError("O objeto não é uma instancia da classe livro")
        return None
    
    def Remover_livro(self, codigo):
        self.__livros = [livro for livro in self.__livros if livro.__codigo != codigo]

    def mostrar_livros(self):
        for livro in self.__livros:
            livro.nome()
        return None