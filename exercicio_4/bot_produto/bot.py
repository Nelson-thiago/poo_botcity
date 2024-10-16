from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

# from .resources.classes.FormularioContato import FormularioContato
from resources.classes.FormularioContato import FormularioContato
from resources.classes.FormularioLogin import FormularioLogin


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

    # patch das páginas HTML locais
    formContato = r"C:\Users\matutino\Desktop\Zl_academy\LG academy\orientacao_obj\exercicio_4\bot_produto\resources\Forms\FormContato.html"
    formLogin = r"C:\Users\matutino\Desktop\Zl_academy\LG academy\orientacao_obj\exercicio_4\bot_produto\resources\Forms\FormLogin.html"
    bot.wait(3000)


    contato = FormularioContato("Formulário de Contato")
    contato.set_nome("João Silva")
    contato.set_email("joao.silva@email.com")
    # contato.exibir()
    print("\n")
    login = FormularioLogin("Formulário de Login")
    login.set_usuario("joaosilva")
    login.set_senha("senha123")
    # login.exibir()

    #Preenchendo FormularioContato
    bot.browse(formContato)
    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(contato.get_nome())
    bot.find_element('//*[@id="email"]', By.XPATH).send_keys(contato.get_email())  # O preço será formatado pelo formulário
    bot.wait(3000)
    # Clica no botão "Enviar" para simular o envio do formulário
    bot.find_element("//input[@type='submit']", By.XPATH).click()

    #Preenchendo FormularioLogin
    bot.browse(formLogin)
    bot.find_element('//*[@id="usuario"]', By.XPATH).send_keys(login.get_usuario())
    bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(login.get_senha())  # O preço será formatado pelo formulário
    bot.wait(3000)
    # Clica no botão "Enviar" para simular o envio do formulário
    bot.find_element("//input[@type='submit']", By.XPATH).click()


    # # Exibe as informações do produto no terminal
    # contato.exibir()
    # login.exibir()
    # Aguarda antes de fechar o navegador
    bot.wait(3000)

    # Fecha o navegador
    bot.stop_browser()

if __name__ == '__main__':
    main()
