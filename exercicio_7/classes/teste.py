
import sys
sys.stdout.reconfigure(encoding='utf-8')
from aluno import Aluno
from curso import Curso
from escola import Escola
def reflexao():
    print("Perguntas para Reflexão:")
    print("1. Como a composição facilita a criação de relações complexas entre objetos?")
    print("Resposta: A composição permite que objetos sejam construídos como uma coleção de outros objetos, facilitando a criação de relações complexas ao agregar funcionalidades e comportamentos de outras classes sem a rigidez da herança. Isso permite que objetos trabalhem juntos e sejam facilmente substituídos ou modificados.")
    
    print("\n2. Qual é a vantagem de usar composição em vez de herança neste exercício?")
    print("Resposta: A composição proporciona maior flexibilidade, pois permite criar estruturas modulares em que os objetos podem ser combinados de diferentes maneiras. Neste exercício, ela evita o acoplamento excessivo entre as classes e facilita a reutilização, permitindo que, por exemplo, um curso tenha uma lista de alunos sem a necessidade de uma hierarquia rígida.")
    
    print("\n3. Como o encapsulamento é utilizado nas classes Aluno, Curso e Escola?")
    print("Resposta: O encapsulamento é aplicado por meio de atributos privados e métodos acessores (getters e setters) para proteger os dados internos das classes e expor apenas o necessário. Nas classes Aluno, Curso e Escola, isso garante que atributos sensíveis, como matrícula e lista de alunos, sejam manipulados de forma controlada, preservando a integridade dos dados e simplificando a interface para o usuário.")
    
    print("\n4. Como você pode estender este sistema para incluir novas funcionalidades, como notas dos alunos e professores para cada curso?")
    print("Resposta: Para incluir notas dos alunos, pode-se adicionar um atributo para armazenar notas e métodos para manipular esses dados. Para incluir professores, seria possível criar uma classe Professor e associá-la ao Curso. Esse sistema modular torna a adição de novas funcionalidades intuitiva, pois novas classes e atributos podem ser incorporados sem modificar a estrutura existente.")


def main():
    
    #Criando alguns alunos:
    aluno1 = Aluno("João", "2023001")
    aluno2 = Aluno("Maria", "2023002")
    
    print(f"\nExibindo informações dos alunos individualmente:")
    aluno1.mostrar_info()
    aluno2.mostrar_info()

    print(f"\nCriando um curso e adicionando alunos:")
    curso = Curso("Matematica", "MAT101")
    curso.adicionar_aluno(aluno1)
    curso.adicionar_aluno(aluno2)

    print(f"\nListando os alunos do curso:")
    curso.mostrar_alunos()

    # Removendo um aluno por matrícula
    curso.Remover_aluno("2023001")

    print(f"\nApós remover o aluno com matrícula 2023001:")
    curso.mostrar_alunos()

    # Criando uma escola e adicionando o curso
    escola = Escola("Escola Central")
    escola.adicionar_curso(curso)

    print("\nListando os cursos na escola:")
    escola.mostrar_cursos()

    reflexao()

if __name__ == "__main__":
    main()
