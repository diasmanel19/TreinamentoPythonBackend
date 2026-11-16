# Funções Anônimas (Lambdas)

#soma = lambda x, y : x + y

#print(soma(5,5))

numeros = [1,2,3,4,5]

triplicados = map(lambda numero : numero * 3, numeros)

print(list(triplicados))