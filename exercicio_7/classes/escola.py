from curso import Curso
class escola:

    def __init__(self, nome, cursos=None):
        self.__nome = nome
        self.__cursos = cursos if cursos is not None else []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cursos(self):
        return self.__cursos

    def adicionar_curso(self, curso):
        if isinstance(curso, Curso):
            self.__cursos.append(curso)
            print(f"Curso {curso.nome} adicionado com sucesso!")
        else:
            raise ValueError("O objeto não é uma instância da classe Curso")

    def mostrar_cursos(self):
        if not self.__cursos:
            print("Nenhum curso disponível.")
        else:
            for curso in self.__cursos:
                print(f"Curso: {curso.nome}, Código: {curso.codigo}")
    
    