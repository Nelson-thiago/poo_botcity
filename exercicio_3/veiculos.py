class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacao(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}')