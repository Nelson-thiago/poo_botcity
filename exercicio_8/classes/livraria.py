from autor import Autor

class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado ao inventário.')

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f'O livro "{titulo}" não foi encontrado no inventário.')

    def mostrar_inventario(self):
        print("Inventário da livraria:")
        for livro in self.livros:
            livro.mostrar_info()