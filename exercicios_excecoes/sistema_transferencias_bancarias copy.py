class Conta:
    def __init__(self, titulo, saldo=0.0, limite=None):
        self.__titulo = titulo
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f'\nDepositado R${valor} na conta de {self.titulo}\nSaldo atual: {self.saldo}\n')
        else:
            raise ValorDeTransferenciaInvalido

    def sacar(self,valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError
        elif valor > self.limite:
            raise LimiteExcedidoError
        else:
            self.saldo -= valor
            print(f'\nSacado R${valor} da conta.\nSaldo atual: {self.saldo}')

    def transferir(self,conta,valor):
        if not isinstance(conta,Conta):
            raise ContaDestinoInvalidaError
        if valor > self.saldo:
            raise SaldoInsuficienteError
        elif valor > self.limite:
            raise LimiteExcedidoError
        else:
            self.saldo -= valor
            conta.saldo += valor
            print(f'\nTransferido R${valor} da conta para {conta.titulo}\nSaldo atual: {self.saldo}')


class SaldoInsuficienteError(Exception):
    def __init__(self, message="Saldo insuficiente para realizar a operação."):
        super().__init__(message)

class LimiteExcedidoError(Exception):
    def __init__(self, message="O valor excede o limite da conta."):
        super().__init__(message)

class ContaDestinoInvalidaError(Exception):
    def __init__(self, message="A conta de destino é inválida ou inexistente."):
        super().__init__(message)

class ValorDeTransferenciaInvalido(Exception):
    def __init__(self, message="O Valor da transação não é válido."):
        super().__init__(message)


def testar_depositar():
    print("---------------------------------\nTeste depositar iniciado\n---------------------------------")
    try:
        conta = Conta('Carlos', saldo=100)
        conta.depositar(-200.5)
    except ValorDeTransferenciaInvalido as e:
        print('Teste 1 de depósito finalizado: Exceção capturada corretamente.')
        print(f"Exceção capturada durante o teste de depósito: {e}\n")
    else:
        print('Erro: Teste de depósito não levantou exceção para valor negativo.\n')

    try:
        conta = Conta('Carlos', saldo=100)
        conta.depositar(200.5)
        print("Teste 2 de deposito finalizado com sucesso: Deposito realizado corretamente\n")
    except ValueError as e:
        print('Teste de depósito finalizado: Exceção capturada corretamente.')
        print(f"Exceção capturada durante o teste de depósito: {e}\n")

def testar_sacar():
    print("---------------------------------\nTeste sacar iniciado\n---------------------------------")
    conta = Conta('Lucas', saldo=200, limite=150)

    try:
        conta.sacar(300)
    except (SaldoInsuficienteError, LimiteExcedidoError) as e:
        print("Teste 1 de saque finalizado: Exceção capturada corretamente.")
        print(f"Exceção capturada durante o teste de saque: {e}\n")
    else:
        print("Erro: Teste de saque não levantou exceção quando deveria.\n")

    try:
        conta.sacar(200)
    except LimiteExcedidoError as e:
        print("Teste 2 de saque finalizado: Exceção de limite capturada corretamente.")
        print(f"Exceção capturada durante o teste de saque: {e}\n")
    else:
        print("Erro: Teste de saque não levantou exceção de limite.\n")

    try:
        conta.sacar(50)
        print("Teste 3 de saque finalizado com sucesso: Saque realizado corretamente.\n")
    except (SaldoInsuficienteError, LimiteExcedidoError) as e:
        print("Erro: Exceção inesperada capturada durante o teste de saque.")
        print(f"Exceção: {e}\n")

def testar_transferir():
    print("---------------------------------\nTeste transferir iniciado\n---------------------------------")

    conta_origem = Conta('Nelson Thiago', saldo=500, limite=300)
    conta_destino = Conta('Caio Faneco', saldo=200, limite=50)

    try:
        conta_origem.transferir(conta_destino, 600)
    except SaldoInsuficienteError as e:
        print("Teste 1 de transferência finalizado: Exceção de saldo insuficiente capturada corretamente.")
        print(f"Exceção capturada durante o teste de transferência: {e}\n")
    else:
        print("Erro: Teste de transferência não levantou exceção para saldo insuficiente.\n")

    try:
        conta_origem.transferir(conta_destino, 400)
    except LimiteExcedidoError as e:
        print("Teste 2 de transferência finalizado: Exceção de limite capturada corretamente.")
        print(f"Exceção capturada durante o teste de transferência: {e}\n")
    else:
        print("Erro: Teste de transferência não levantou exceção para limite excedido.\n")

    try:
        conta_origem.transferir(conta_destino, 100)
        print("Teste 3 de transferência finalizado com sucesso: Transferência realizada corretamente.\n")
    except (SaldoInsuficienteError, LimiteExcedidoError, ContaDestinoInvalidaError) as e:
        print("Erro: Exceção inesperada capturada durante o teste de transferência.\n")
        print(f"Exceção: {e}")


testar_depositar()
testar_sacar()
testar_transferir()