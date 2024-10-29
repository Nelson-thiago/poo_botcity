import sys
sys.stdout.reconfigure(encoding='utf-8')

from functools import reduce

class Venda:
    def __init__(self, nome_produto, quantidade, preco_unitario):
        self.__nome_produto = nome_produto
        self.__quantidade = quantidade
        self.__preco_unitario = preco_unitario
    
    def total_venda(self):
        return self.quantidade * self.preco_unitario

    @property
    def nome_produto(self):
        return self.__nome_produto

    @nome_produto.setter
    def nome(self, nome_produto):
        self.__nome_produto = nome_produto
    
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario
        
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

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
