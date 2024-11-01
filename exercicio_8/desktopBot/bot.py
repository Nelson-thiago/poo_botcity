from botcity.core import DesktopBot
import subprocess
from botcity.maestro import *
from faker import Faker
import random

fake = Faker()

def gerar_livros(num_livros):
    livros = []
    for _ in range(num_livros):
        livro = {
            "titulo": fake.text(max_nb_chars=20),
            "codigo": fake.random_int(min=1000, max=9999)
        }
        livros.append(livro)
    return livros

def gerar_clientes(num_clientes):
    clientes = []
    for _ in range(num_clientes):
        cliente = {
            "nome": fake.name()
        }
        clientes.append(cliente)
    return clientes

def criar_livro(bot, livro):
    if not bot.find("texto titulo", matching=0.97, waiting_time=10000):
        not_found("texto titulo")
    bot.click_relative(57, 44)
    bot.paste(livro["titulo"])

    if not bot.find("codigo livro", matching=0.97, waiting_time=10000):
        not_found("codigo livro")
    bot.click_relative(39, 43)
    bot.paste(str(livro["codigo"]))

    if not bot.find("adicionar livro", matching=0.97, waiting_time=10000):
        not_found("adicionar livro")
    bot.click()

    if not bot.find("fechar_dialog", matching=0.97, waiting_time=10000):
        not_found("fechar_dialog")
    bot.click()

def emprestar_livro(bot, livro, cliente):
    if not bot.find("codigo emprestimo", matching=0.97, waiting_time=10000):
        not_found("codigo emprestimo")
    bot.click_relative(103, 34)
    bot.paste(str(livro["codigo"]))

    if not bot.find("nome_cliente", matching=0.97, waiting_time=10000):
        not_found("nome_cliente")
    bot.click_relative(-5, 41)
    bot.paste(cliente["nome"])

    if not bot.find("botao_emprestar", matching=0.97, waiting_time=10000):
        not_found("botao_emprestar")
    bot.click()

    if not bot.find("fechar_dialog", matching=0.97, waiting_time=10000):
        not_found("fechar_dialog")
    bot.click()

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    num_livros = 3  
    livros = gerar_livros(num_livros)
    clientes = gerar_clientes(num_livros)  

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    process = subprocess.Popen(["python", r"C:\Users\matutino\Desktop\Zl_academy\LG academy\orientacao_obj\exercicio_8\appTkinter.py"])

    if not bot.find("maximizar", matching=0.97, waiting_time=10000):
        not_found("maximizar")
    bot.click()

    for livro in livros:
        criar_livro(bot, livro)

    for i, livro in enumerate(livros):
        cliente = clientes[i]
        emprestar_livro(bot, livro, cliente)

    if not bot.find("listar_livros", matching=0.97, waiting_time=10000):
        not_found("listar_livros")
    bot.click()

    bot.wait(10000)

    if not bot.find("fechar lista", matching=0.97, waiting_time=10000):
        not_found("fechar lista")
    bot.click()
    bot.wait(3000)

    print("\nLista de Livros Emprestados:")
    for i, livro in enumerate(livros):
        print(f"Título: {livro['titulo']}, Código: {livro['codigo']}, Cliente: {clientes[i]['nome']}")

    process.terminate()

    # Descomente para finalizar a tarefa no BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
