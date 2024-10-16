from .FormBase import FormBase
# Subclasse: FormularioContato
class FormularioContato(FormBase):
    def __init__(self, titulo, nome="", email=""):
        super().__init__(titulo)   
        self.__nome = nome         
        self.__email = email     

    # Getters e setters para os campos de contato
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Método para mostrar infos do formulário de contato
    def exibir(self):
        print("Exibindo contato...")
        print(f"Nome: {self.get_nome()}")
        print(f"Email: {self.get_email()}")
        self.mostrar_informacoes()
