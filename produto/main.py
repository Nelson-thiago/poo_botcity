from produto.bot_produto.Produto import Produto  
if "__main__":
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
