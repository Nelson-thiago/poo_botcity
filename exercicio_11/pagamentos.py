from abc import ABC,abstractmethod
class pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass
    
    def detalhes_pagamento(self):
        print(f"processando pagamento via {self.__class__.__name__}")

class pagamentoPix(pagamento):
    def processar_pagamento(self):
        print("processando pagamento via Pix")

class pagamentoBoleto(pagamento):
    def processar_pagamento(self):
        print("processando pagamento via Boleto")

class pagamentoCarataoCredito(pagamento):
    def processar_pagamento(self):
        print("processando pagamento via Cartão de Crédito")


def testarPagamento():
    pix = pagamentoPix()
    boleto = pagamentoBoleto()
    cartao_credito = pagamentoCarataoCredito()


    pix.processar_pagamento()             
    boleto.processar_pagamento()          
    cartao_credito.processar_pagamento()   

    pix.detalhes_pagamento()             
    boleto.detalhes_pagamento()          
    cartao_credito.detalhes_pagamento()   

# Testar a função
testarPagamento()
