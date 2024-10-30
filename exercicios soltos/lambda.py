produtos =[
    {"nome":"camisa", 'preco':20},
    {"nome":"bayoneta", 'preco':34},
    {"nome":"morningstar", 'preco':100}
]
#ordena preços de produtos
produtos_ordenados = sorted(produtos, key=lambda produto: produto['preco'])
print(produtos_ordenados)

numeros = [1,3,5,7,9]
dobrados=list(map(lambda x: x * 2, numeros))
print(dobrados)

temperatura_celcius = [0, 20, 37, 100]
temperatura_fahrenheith=list(map(lambda c:c*9/5 + 32, temperatura_celcius))
print(temperatura_fahrenheith)

numeros = [1,3,5,7,9]
numeros_quadrados=list(map(lambda x: x ** 2, numeros))
print(numeros_quadrados)

#filter
#filtrar numeros pares
numeros=[1,2,3,4,5,6,7,8,9]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

#filtar palavras com mais de 5 letras
palavras = ["python", "é", "incrivel", "para", 'data', 'science']
palavras_longas = list(filter(lambda palavra: len(palavra) > 5, palavras))
print(palavras_longas)

#reduce
from functools import reduce
#filtar palavras com mais de 5 letras
numeros = [1,3,5,7,9]
numeros_quadrados=list(map(lambda x: x ** 2, numeros))
print(numeros_quadrados)

#list compreheisions
numeros = [1,2,3,4,5,6,7,8,9] 
quadrados = [x **2 for x in numeros]
print(quadrados)

#dictionary compreheisions
numeros = [1,2,3,4,5,6,7,8,9] 
quadrados_dict = {x:x **2 for x in numeros}
print(quadrados_dict)

#set compreheisions
numeros = [1,2,2,2,3,4,5,5,5,5,6,7,8,8,8,8,9] 
quadrados_set = {x **2 for x in numeros}
print(quadrados_set)

#decorator
def saudacao_decorator(func):
    def wrapper(nome):
        print('Olá!')
        func(nome)
        print('Tenha um bom dia!')
    return wrapper

@saudacao_decorator
def saudacao(nome):
    print(f"Prazer em conhece-lo, {nome}.")

saudacao('alice')

#Decorator com argumentos
def multiplicar_por(n):
    def decorator(func):
        def wrapper(x):
            return func(x) * n
        return wrapper
    return decorator

@multiplicar_por(3)
def soma_2(x):
    return x+2

print(soma_2(5))

def gerar_pares(limite):
    n=0
    while n<limite:
        yield n 
        n+=2
for numeros in gerar_pares(10):
    print(numeros)

#geradores e iteradores
class Contador:
    def __init__(self,limite):
        self.limite = limite
        self.n = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <self.limite:
            resultado = self.n
            self.n += 1
            return resultado
        else:
            raise StopIteration
        
contador =Contador(5)
for numero in contador:
    print(numero)


class IteradorDeNomes:
    def __init__(self, nomes):
        self.nomes = nomes
        self.indice = 0

    def __iter__(self):
        #retorna o proprio objeto como iterador
        return self
    
    def __next__(self):
        #retorna o proximo nome em maiusculas, se disponivel
        if self.indice < len(self.nomes):
            nome = self.nomes[self.indice].upper()
            self.indice += 1
            return nome
        else:
            #levanta Stopiteration ao final da lista
            raise StopIteration
        
# Usa o iterador `IteradorDeNomes`
nomes = IteradorDeNomes(["Alice", "Bob", "Charlie"])
for nome in nomes:
    print(nome)