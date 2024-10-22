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


pix = pagamentoPix()
boleto = pagamentoBoleto()
cartao_credito = pagamentoCarataoCredito()

realizar_pagamento(pix)             
realizar_pagamento(boleto)          
realizar_pagamento(cartao_credito)   