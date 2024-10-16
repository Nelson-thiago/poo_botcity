# Superclasse: FormBase
class FormBase:
    def __init__(self, titulo):
        self.__titulo = titulo  

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def mostrar_informacoes(self):
        print(f"Formulário: {self.__titulo}")
