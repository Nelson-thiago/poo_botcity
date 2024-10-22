from flask import Flask, request, render_template, redirect, url_for, flash
import sys
import os

# Atualizando o caminho para incluir a pasta "classes"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'classes')))

from autor import Autor  # Importar a classe Autor
from livro import Livro  # Importar a classe Livro
from biblioteca import Biblioteca  # Importar a classe Biblioteca

app = Flask(__name__)
app.secret_key = 'seu_segredo_aqui'  # Necessário para flash messages

# Instanciando autores
autor1 = Autor(codigo="001", nome="George Orwell")
autor2 = Autor(codigo="002", nome="J.R.R. Tolkien")

# Instanciando livros
livro1 = Livro(codigo="1001", titulo="1984", autor=autor1, disponibilidade=True)
livro2 = Livro(codigo="1002", titulo="O Senhor dos Anéis", autor=autor2, disponibilidade=True)

# Instanciando a biblioteca e adicionando os livros
biblioteca = Biblioteca("Minha Biblioteca")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

@app.route('/emprestar', methods=['GET', 'POST'])
def emprestar_livro():
    if request.method == 'POST':
        codigo_livro = request.form['codigo_livro']
        nome_cliente = request.form['nome_cliente']

        # Registrar o empréstimo
        try:
            biblioteca.registrar_emprestimo(codigo_livro, nome_cliente)
            flash(f'Empréstimo do livro {codigo_livro} registrado com sucesso para {nome_cliente}!', 'success')
        except ValueError as e:
            flash(str(e), 'error')  # Exibir mensagem de erro caso haja problema

        return redirect(url_for('emprestar_livro'))  # Redireciona para a mesma página

    return render_template('emprestar.html')  # Renderiza a página de empréstimo


# @app.route('/listar_veiculos')
# def listar_veiculos():
#     return render_template('veiculos.html', dados=Veiculo.lista_veiculos)


@app.route('/emprestar_livro')
def alugar_carros():
    return render_template('emprestar.html')

@app.route('/')
def index():
    return render_template('menu.html')


# @app.route('/alugar_motos')
# def alugar_motos():
#     return render_template('motocicleta.html')

if __name__ == "__main__":
    app.run(debug=True)
