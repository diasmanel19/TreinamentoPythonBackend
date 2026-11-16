# Atividade Pratique: Calculadora com Tratamento de Exceções e Funções Lambda

# Defina cada operação matemática (soma, subtração, multiplicação, divisão) como uma função lambda separada.
operadores = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Não pode dividir por zero!"
}

#Crie uma lista com os nomes das operações disponíveis (por exemplo ["Soma", "Subtração", "Multiplicação", "Divisão"]).
matematica = ["Soma", "Subtração", "Multiplicação", "Divisão"]

#Use list comprehension para gerar as linhas do menu numeradas dinamicamente a partir dessa lista (por exemplo, transformando cada item da lista em uma string como "1 - Soma").
opcoes = [f"{i} - {item}" for i, item in enumerate(matematica, 1)]

print("\n".join(opcoes))

def calculadora():
#Escreva a lógica para pedir ao usuário dois números, usando try-except ao redor da conversão (int()) para capturar o erro quando o usuário digitar algo que não é número.
    while True:
        try:
            numero_um = int(input("Diga o primeiro número: "))
            operador = input("Escolha a operação (+, -, *, /): ").strip()
            numero_dois = int(input("Diga o segundo número: "))

            if operador in operadores:
                funcao_calculo = operadores[operador]
                resultado = funcao_calculo(numero_um, numero_dois)
                print(f"O resultado de {numero_um} {operador} {numero_dois} é: {resultado}")
            else:
                print("Operador inválido! Tente novamente.")

#Se a conversão falhar, exiba uma mensagem de erro e peça o valor novamente, repetindo até que o usuário digite um número válido.               
        except ValueError:
            print("Este número não é válido, tente novamente")

#Pergunte ao usuário se ele deseja realizar outra operação; se sim, volte ao menu, se não, encerre o programa.
        continuar = input("\nDeseja realizar outra operação? (s/n): ").strip().lower()
        if continuar != 's':
            print("Fim do calculo")
            break

if __name__ == "__main__":
    calculadora()