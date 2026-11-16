#receba um numero e determine se é um palindromo

numero_normal = int(input())

numero_invertido = str(numero_normal)

inversao = numero_invertido[::-1]

if str(numero_normal) == inversao: 
    print("é palíndromo") 
else: 
    print("não é palindromo")