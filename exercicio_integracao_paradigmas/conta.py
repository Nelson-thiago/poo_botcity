import sys
sys.stdout.reconfigure(encoding='utf-8')

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

    def filtrar_transacoes_por_tipo(self, tipo):
        return list(filter(lambda t: t.tipo == tipo, self.transacoes))

    def aplicar_taxa(self, taxa):
        self.transacoes = list(map(lambda t: Transacao(t.tipo, t.valor * (1 - taxa)) if t.tipo == "Saque" else t, self.transacoes))

class Conta:
    def __init__(self, tipo, valor_inicial=0):
        self.tipo = tipo
        self.valor = valor_inicial
        self.historico = HistoricoDeTransacoes()

    def adicionar_transacao(self, tipo, valor):
        transacao = Transacao(tipo, valor)
        self.historico.adicionar_transacao(transacao)

    def aplicar_taxa_a_saques(self, taxa):
        self.historico.aplicar_taxa(taxa)

    def gerar_extrato(self):
        return list(self.historico.gerar_extrato())



conta = Conta(tipo="Corrente", valor_inicial=0)

conta.adicionar_transacao("Depósito", 1000)
conta.adicionar_transacao("Depósito", 500)
conta.adicionar_transacao("Depósito", 750)
conta.adicionar_transacao("Depósito", 1200)
conta.adicionar_transacao("Depósito", 600)

conta.adicionar_transacao("Saque", 200)
conta.adicionar_transacao("Saque", 300)
conta.adicionar_transacao("Saque", 150)
conta.adicionar_transacao("Saque", 400)
conta.adicionar_transacao("Saque", 250)

print("Transações antes da taxa:")
for transacao in conta.gerar_extrato():
    print(transacao)

# Aplicar taxa 10%  
conta.aplicar_taxa_a_saques(0.1)

print("\nTransações depois da taxa:")
for transacao in conta.gerar_extrato():
    print(transacao)

saques = conta.historico.filtrar_transacoes_por_tipo("Saque")
print("\nApenas saques após a aplicação da taxa:")
for saque in saques:
    print(f"{saque.tipo}: {saque.valor}")
