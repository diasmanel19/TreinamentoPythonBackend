# Crie uma classe Pagamento com um método processar().
class pagamento:
    def processar(self):
        print("Pagamento realizado!")

# Crie duas classes que herdem dela:
class pix(pagamento):
    def processar(self):
        return "Pagamento realizado via Pix!"

class cartao(pagamento):
    def processar(self):
        return "Pagamento realizado via Cartão!"

metodos = [pix(), cartao()]

for metodo in metodos:
    print(metodo.processar())