class braco:

    def __init__(self, nome):
        self.nome = nome

    def supino(self):
        print(f"{self.nome} está fazendo supino ")
        

class cardio(braco):

    def correr(self):
        print(f"{self.nome} está correndo ")

meu_nome = braco("Emanuel")
meu_nome = cardio("Emanuel")

meu_nome.supino()
meu_nome.correr()  




