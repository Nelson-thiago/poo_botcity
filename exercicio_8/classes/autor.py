
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
        from livro import Livro 
        if isinstance(livro, Livro):
            self.__livros.append(livro)
            print(f'Livro "{livro.titulo}" adicionado ao autor {self.__nome}.')
        else:
            raise ValueError("O objeto fornecido não é uma instância da classe Livro.")

    
    def Remover_livro(self, codigo):
        from livro import Livro 
        self.__livros = [livro for livro in self.__livros if livro.__codigo != codigo]

    def mostrar_livros(self):
        from livro import Livro 
        if self.__livros:
            print(f'Livros escritos por {self.__nome}:')
            for livro in self.__livros:
                print(f'- {livro.titulo}')
        else:
            print(f'{self.__nome} ainda não tem livros cadastrados.')