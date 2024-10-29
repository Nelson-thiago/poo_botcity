import sys
sys.stdout.reconfigure(encoding='utf-8')

from functools import reduce

class Venda:
    def __init__(self, nome_produto, quantidade, preco_unitario):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
    
    def total_venda(self):
        return self.quantidade * self.preco_unitario

class HistoricoVendas:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_por_produto(self):
        totais = {}
        for venda in self.vendas:
            totais[venda.nome_produto] = reduce(
                lambda acc, v: acc + (v.quantidade * v.preco_unitario),
                filter(lambda x: x.nome_produto == venda.nome_produto, self.vendas),
                0
            )
        return totais

    def listar_vendas_acima_de(self, valor):
        for venda in self.vendas:
            if venda.total_venda() > valor:
                yield venda

# Exemplo de uso
venda1 = Venda("Produto A", 10, 5.0)
venda2 = Venda("Produto A", 20, 4.0)
venda3 = Venda("Produto B", 5, 10.0)

historico = HistoricoVendas()
historico.adicionar_venda(venda1)
historico.adicionar_venda(venda2)
historico.adicionar_venda(venda3)

print("Total por produto:", historico.total_por_produto())
print("Vendas acima de 30:")
for venda in historico.listar_vendas_acima_de(30):
    print(f"{venda.nome_produto} - Total: {venda.total_venda()}")
