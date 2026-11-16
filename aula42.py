# Try Except

try:
    numero_um = int(input("Digite o primeiro numero: "))
    numero_dois = int(input("Digite o segundo numero: "))

    resultado = numero_um + numero_dois

    print(resultado)
except ValueError:
    print("Digite o valor corretamente!")
