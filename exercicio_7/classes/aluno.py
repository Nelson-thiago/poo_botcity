class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def mostrar_info(self):
        matricula = self.__matricula
        nome = self.__nome
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print(f"nome do aluno: {nome}\nMatricula do aluno: {matricula}")
        return matricula, nome
