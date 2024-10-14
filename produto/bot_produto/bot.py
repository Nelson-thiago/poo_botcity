from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
# Agora você pode importar a classe Produto
from Produto import Produto

def salvar_produto_em_arquivo(produto, filename='produtos.txt'):
    with open(filename, 'a') as file:  # Abre o arquivo em modo de anexação
        file.write(f"Nome: {produto.obter_nome()}\n")
        file.write(f"Preço: R$ {produto.obter_preco():.2f}\n")
        file.write(f"Quantidade: {produto.obter_qnt()}\n")
        file.write("-" * 20 + "\n")  # Adiciona uma linha separadora


def main():
    # Inicializa o bot
    bot = WebBot()
    bot.headless = False  # Para ver o navegador durante a automação
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    # Acessa a página HTML local
    bot.browse(r"C:\Users\matutino\Desktop\Zl_academy\LG academy\orientacao_obj\produto\form.html")

    # Aguarda o carregamento da página
    bot.wait(3000)

    # Preenche os campos do formulário com dados de exemplo
    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys('Notebook')
    bot.find_element('//*[@id="preco"]', By.XPATH).send_keys('250000')  # O preço será formatado pelo formulário
    bot.find_element('//*[@id="qnt"]', By.XPATH).send_keys('5')
    bot.wait(3000)


    # Clica no botão "Enviar" para simular o envio do formulário
    bot.find_element("//input[@type='submit']", By.XPATH).click()

    # Após o envio, captura os valores do formulário
    nome = bot.find_element('//*[@id="nome"]', By.XPATH).get_attribute('value')
    preco = bot.find_element('//*[@id="preco"]', By.XPATH).get_attribute('value')
    qnt = bot.find_element('//*[@id="qnt"]', By.XPATH).get_attribute('value')

    # Remove a formatação do preço
    preco = float(preco.replace('R$', '').replace('.', '').replace(',', '.'))

    # Converte a quantidade para inteiro
    qnt = int(qnt)

    # Cria o objeto Produto com os dados coletados
    produto = Produto(nome, preco, qnt)

    # Exibe as informações do produto no terminal
    produto.exibir_info()

    # Salva as informações do produto em um arquivo .txt
    salvar_produto_em_arquivo(produto)

    # Aguarda antes de fechar o navegador
    bot.wait(3000)

    # Fecha o navegador
    bot.stop_browser()

if __name__ == '__main__':
    main()
