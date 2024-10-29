import sys
sys.stdout.reconfigure(encoding='utf-8')

class Conta:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        self.transacoes.append({"tipo": tipo, "valor": valor})

    def filtrar_transacoes_por_tipo(self, tipo):
        return list(filter(lambda transacao: transacao["tipo"] == tipo, self.transacoes))

    def aplicar_taxa(self, taxa):
        self.transacoes = list(
            map(lambda transacao: {"tipo": transacao["tipo"],
                                   "valor": transacao["valor"] * (1 - taxa) if transacao["tipo"] == "Saque" else transacao["valor"]},
                self.transacoes)
        )

# Exemplo de uso
conta = Conta()
conta.adicionar_transacao("Depósito", 1000)
conta.adicionar_transacao("Saque", 200)
conta.adicionar_transacao("Saque", 300)

print("Transações antes da taxa:", conta.transacoes)

# Aplicar taxa de 10% aos saques
conta.aplicar_taxa(0.1)

print("Transações depois da taxa:", conta.transacoes)

# Filtrar apenas saques
print("Apenas saques:", conta.filtrar_transacoes_por_tipo("Saque"))
