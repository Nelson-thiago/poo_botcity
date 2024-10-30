
from botcity.core import DesktopBot
import subprocess
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    process = subprocess.Popen(["python", r"C:\Users\matutino\Desktop\Zl_academy\LG academy\orientacao_obj\exercicio_8\appTkinter.py"])
    
    if not bot.find( "maximizar", matching=0.97, waiting_time=10000):
        not_found("maximizar")
    bot.click()
    
    if not bot.find( "texto titulo", matching=0.97, waiting_time=10000):
        not_found("texto titulo")
    bot.click_relative(57, 44)
    bot.paste("o menino maluquinho")
    
    if not bot.find( "codigo livro", matching=0.97, waiting_time=10000):
        not_found("codigo livro")
    bot.click_relative(39, 43)
    bot.paste("2024")
    
    if not bot.find( "adicionar livro", matching=0.97, waiting_time=10000):
        not_found("adicionar livro")
    bot.click()
    
    if not bot.find( "fechar_dialog", matching=0.97, waiting_time=10000):
        not_found("fechar_dialog")
    bot.click()
    
    if not bot.find( "codigo emprestimo", matching=0.97, waiting_time=10000):
        not_found("codigo emprestimo")
    bot.click_relative(103, 34)
    bot.paste("2024")
    
    if not bot.find( "botao_emprestar", matching=0.97, waiting_time=10000):
        not_found("botao_emprestar")
    bot.click()
    
    if not bot.find( "fechar_dialog", matching=0.97, waiting_time=10000):
        not_found("fechar_dialog")
    bot.click()
    
    if not bot.find( "codigo_devolucao", matching=0.97, waiting_time=10000):
        not_found("codigo_devolucao")
    bot.click_relative(103, 35)
    bot.paste("2024")

    if not bot.find( "botao_devolver", matching=0.97, waiting_time=10000):
        not_found("botao_devolver")
    bot.click()
    
    if not bot.find( "fechar_dialog", matching=0.97, waiting_time=10000):
        not_found("fechar_dialog")
    bot.click()
    
    if not bot.find( "listar_livros", matching=0.97, waiting_time=10000):
        not_found("listar_livros")
    bot.click()
    
    bot.wait(10000)

    
    if not bot.find( "fechar lista", matching=0.97, waiting_time=10000):
        not_found("fechar lista")
    bot.click()
    bot.wait(3000)
    
    
    bot.wait(3000)

    # Para o aplicativo
    process.terminate()
    ...

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()










