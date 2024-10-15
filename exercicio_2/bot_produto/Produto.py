class Produto:
    def __init__(self, nome, preco, qnt):
        self._nome = nome          # Atributo privado
        self._preco = preco        # Atributo privado
        self._qnt = qnt            # Atributo privado

    def exibir_info(self):
        """Exibe as informações do produto."""
        info = f"Nome: {self._nome}\nPreço: R$ {self._preco:.2f}\nQuantidade: {self._qnt}"
        print(info)

    def atualizar_preco(self, novo_preco):
        """Atualiza o preço do produto se o novo preço for válido."""
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = novo_preco
        print(f"Preço atualizado para R$ {self._preco:.2f}")

    def atualizar_qnt(self, nova_qnt):
        """Atualiza a quantidade do produto se a nova quantidade for válida."""
        if nova_qnt < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._qnt = nova_qnt
        print(f"Quantidade atualizada para {self._qnt}")

    def obter_nome(self):
        """Retorna o nome do produto."""
        return self._nome

    def obter_preco(self):
        """Retorna o preço do produto."""
        return self._preco

    def obter_qnt(self):
        """Retorna a quantidade do produto."""
        return self._qnt

# Exemplo de uso da classe Produto
if __name__ == "__main__":
    produto = Produto("Livro de Python", 49.90, 10)
    
    # Exibir informações do produto
    produto.exibir_info()
    
    # Atualizar preço e quantidade
    try:
        produto.atualizar_preco(39.90)
        produto.atualizar_qnt(8)
    except ValueError as e:
        print(e)
    
    # Exibir informações atualizadas
    produto.exibir_info()
    
    # Acessando atributos usando métodos
    print(f"Nome do produto: {produto.obter_nome()}")
    print(f"Preço do produto: R$ {produto.obter_preco():.2f}")
    print(f"Quantidade do produto: {produto.obter_qnt()}")
