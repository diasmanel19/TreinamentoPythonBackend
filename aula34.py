#POO

class Moto:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_marca_da_moto(self):
        print(f"A marca da minha moto é: {self.marca}")

    def mostrar_modelo_da_moto(self):
        print(f"O modelo da minha moto é: {self.modelo}")

    def mostrar_ano_da_moto(self):
        print(f"O ano da minha moto é: {self.ano}")

minha_moto = Moto("Yamaha", "Fazer FZ25", 2026)

minha_moto.mostrar_marca_da_moto()
minha_moto.mostrar_modelo_da_moto()
minha_moto.mostrar_ano_da_moto()


