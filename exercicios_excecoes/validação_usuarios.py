class Usuario:
    def __init__(self, nome, idade, email):
        try:
            if not nome:
                raise ValueError("O nome não pode ser vazio.")
            if not isinstance(idade, int):
                raise TypeError("A idade deve ser um número inteiro.")
            if "@" not in email:
                raise ValueError("O email deve conter um '@'.")

            self.nome = nome
            self.idade = idade
            self.email = email
            print(f"Usuário criado com sucesso: {self.nome}, {self.idade}, {self.email}")

        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except TypeError as te:
            print(f"Erro de tipo: {te}")

usuario1 = Usuario("", 25, "email.com")  
usuario2 = Usuario("nelson Thiago", "vinte", "nelson@email.com")  
usuario3 = Usuario("Caio Cezar", 25, "caioemail.com") 
usuario4 = Usuario("carlos souza", 21, "carlos@gmail.com") 
