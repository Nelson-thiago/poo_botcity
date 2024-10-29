import sys
sys.stdout.reconfigure(encoding='utf-8')

class pagamento:
    def fazerPagamento(self):
        pass

class pagamentoPix(pagamento):
    def fazerPagamento(self):
        return "Pagamento feito por Pix"

class pagamentoBoleto(pagamento):
    def fazerPagamento(self):
        return "Pagamento feito por Boleto"

class pagamentoCarataoCredito(pagamento):
    def fazerPagamento(self):
        return "Pagamento feito por Cartão de Crédito"

def realizar_pagamento(metodo):
    print(metodo.fazerPagamento())

def Perguntas():

    print("\n1. O que acontece se você adicionar um novo método de pagamento sem modificar a função processar?")
    print("R: Como a função `realizar_pagamento` utiliza polimorfismo, um novo método de pagamento pode ser adicionado "
          "como uma nova classe que herda de `pagamento` e implementa `fazerPagamento`, sem a necessidade de modificar "
          "a função `realizar_pagamento`. A função processa qualquer método de pagamento que implemente o método "
          "`fazerPagamento`.")

    print("\n2. Como o polimorfismo ajuda a manter o código flexível e extensível?")
    print("R: O polimorfismo permite que diferentes classes compartilhem uma interface comum, ou seja, métodos com o "
          "mesmo nome e comportamento esperado. Assim, novas classes de métodos de pagamento podem ser adicionadas "
          "sem modificar o código existente, tornando o sistema mais flexível e extensível.")

    print("\n3. Qual é a diferença entre a função processar e os métodos processar_pagamento nas subclasses?")
    print("R: A função `realizar_pagamento` é uma função geral que chama o método `fazerPagamento` da instância de "
          "pagamento fornecida, enquanto os métodos `fazerPagamento` nas subclasses representam a implementação específica "
          "de cada método de pagamento (Pix, Boleto, Cartão de Crédito).")

    print("\n4. Como você pode garantir que todos os métodos de pagamento implementem o método processar_pagamento corretamente?")
    print("R: Uma maneira de garantir isso é tornar `fazerPagamento` um método abstrato na classe `pagamento` usando "
          "a biblioteca `abc` (Abstract Base Class), o que forçaria todas as subclasses a implementar esse método.")

pix = pagamentoPix()
boleto = pagamentoBoleto()
cartao_credito = pagamentoCarataoCredito()

realizar_pagamento(pix)             
realizar_pagamento(boleto)          
realizar_pagamento(cartao_credito)   
Perguntas()