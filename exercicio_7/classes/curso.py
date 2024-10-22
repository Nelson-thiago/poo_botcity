from aluno import Aluno
class Curso:

    def __init__(self, nome, codigo, alunos=None):
        self.__nome = nome
        self.__codigo = codigo
        self.__alunos = alunos if alunos is not None else []

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
    def alunos(self):
        return self.__alunos

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            nome_aluno = aluno.nome

            print(f"Aluno {nome_aluno} adicionado com sucesso")
        else:
            ValueError("O objeto não é uma instancia da classe aluno")
        return None
    
    def mostrar_alunos(self):
        for aluno in self.__alunos:
            aluno.mostrar_info()
        return None
    
    def Remover_aluno(self, matricula):
        self.__alunos = [aluno for aluno in self.__alunos if aluno.__matricula != matricula]


# Exemplo de uso:

# Criando alguns alunos
aluno1 = Aluno("João", "2023001")
aluno2 = Aluno("Maria", "2023002")

# Criando um curso e adicionando alunos
curso = Curso("Matemática", "MAT101")
curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)

# Listando alunos do curso
curso.mostrar_alunos()