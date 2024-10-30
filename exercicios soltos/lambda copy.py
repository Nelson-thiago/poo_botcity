class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class HistoricoDeTransacoes:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def gerar_extrato(self):
        for transacao in self.transacoes:
            yield f"{transacao.tipo}: {transacao.valor}"

# Exemplo de uso
historico = HistoricoDeTransacoes()
historico.adicionar_transacao(Transacao("Depósito", 200))
historico.adicionar_transacao(Transacao("Saque", 100))

historico.adicionar_transacao(Transacao("Depósito", 200))
historico.adicionar_transacao(Transacao("Saque", 100))
historico.adicionar_transacao(Transacao("Depósito", 200))
historico.adicionar_transacao(Transacao("Saque", 100))
historico.adicionar_transacao(Transacao("Depósito", 200))
historico.adicionar_transacao(Transacao("Saque", 100))

for transacao in historico.gerar_extrato():
    print(transacao)