#Animal
class Animal:
    def __init__(self, nome, idade):
        self.dados = {'nome': nome, 'idade': idade}

    def emitir_som(self):
        print("O animal emitiu um som genérico.")

    def exibir(self):
        print(self.dados)

#Cachorro
class Cachorro(Animal):
     def emitir_som(self):
        print("O cachorro latiu!")

#Gato
class Gato(Animal):
     def emitir_som(self):
        print("O gato miou!")

#exibição
meu_cachorro = Cachorro('Rex', '2 anos')
meu_gato = Gato('mingau', '1 ano')

meu_cachorro.exibir()
meu_cachorro.emitir_som()

meu_gato.exibir()
meu_gato.emitir_som()



