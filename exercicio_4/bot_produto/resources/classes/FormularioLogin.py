from .FormBase import FormBase
from .FormularioContato import FormularioContato
# Subclasse: FormularioLogin
class FormularioLogin(FormBase):
    def __init__(self, titulo, usuario="", senha=""):
        super().__init__(titulo)  
        self.__usuario = usuario  
        self.__senha = senha      

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

    def exibir(self):
        print("Exibindo usuário...")
        print(f"Usuário: {self.get_usuario()}")
        # Para  exemplo, vai exibir apenas a senha "criptografada"
        print(f"Senha: {'*' * len(self.get_senha())}")  # Mostrando a senha como asteriscos
        self.mostrar_informacoes()


contato = FormularioContato("Formulário de Contato")
contato.set_nome("João Silva")
contato.set_email("joao.silva@email.com")
contato.exibir()

print("\n")

login = FormularioLogin("Formulário de Login")
login.set_usuario("joaosilva")
login.set_senha("senha123")
login.exibir()
