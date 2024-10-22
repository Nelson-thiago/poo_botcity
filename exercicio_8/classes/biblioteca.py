from livro import Livro
class Biblioteca:
    total_livros = 0

    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []
        self.__emprestimos = {}

    @property
    def nome(self):
        return self.__nome

    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.__livros.append(livro)
            Biblioteca.total_livros += 1
            print(f'O livro "{livro.titulo}" foi adicionado à biblioteca "{self.__nome}".')
        else:
            raise ValueError("O objeto fornecido não é uma instância da classe Livro.")

    def registrar_emprestimo(self, codigo_livro, cliente):
        livro = self._buscar_livro_por_codigo(codigo_livro)
        if livro and livro.disponibilidade:
            livro.emprestar()
            self.__emprestimos[codigo_livro] = cliente
        else:
            print(f'O livro com código {codigo_livro} não está disponível para empréstimo.')

    def registrar_devolucao(self, codigo_livro):
        livro = self._buscar_livro_por_codigo(codigo_livro)
        if livro and not livro.disponibilidade:
            livro.devolver()
            del self.__emprestimos[codigo_livro]
        else:
            print(f'O livro com código {codigo_livro} não está emprestado.')

    def mostrar_livros_disponiveis(self):
        print("Livros disponíveis para empréstimo:")
        disponiveis = [livro for livro in self.__livros if livro.disponibilidade]
        if disponiveis:
            for livro in disponiveis:
                print(f'- {livro.titulo} (Código: {livro.codigo})')
        else:
            print("Nenhum livro disponível no momento.")

    @classmethod
    def mostrar_total_livros(cls):
        print(f'Total de livros na biblioteca: {cls.total_livros}')

    def _buscar_livro_por_codigo(self, codigo_livro):
        for livro in self.__livros:
            if livro.codigo == codigo_livro:
                return livro
        print(f'Livro com código {codigo_livro} não encontrado.')
        return None
