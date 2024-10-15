from veiculos import Veiculo  # Importando a classe veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, numPortas):
        super().__init__(marca, modelo)
        self.numPortas = numPortas

    def informacaoCompleta(self):
        self.informacao()
        print(f'Numero de Portas: {self.numPortas}')


carro = Carro("Volkswagem","rg32s",4)
Carro.informacaoCompleta(carro)