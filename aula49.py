# Resolução de problemas - Parte 21
# Dado um array array_legal de tamanho n, retorne o elemento majoritário.
# O elemento majoritário é aquele que aparece mais de [n/2] vezes.
# Você pode assumir que o elemento majoritário sempre existe no array

array_legal = [4, 2, 4, 1, 4, 4, 3, 4, 2, 4, 4]
# n é o tamanho do array_legal
n = len(array_legal)
# item majoritário é o item que parace mais de n/2 vezes
item_majoritario = n / 2

dicionario_legal = {}

for item in array_legal:
    if item not in dicionario_legal:
        dicionario_legal[item] = 1
    else:
        dicionario_legal[item] += 1


for chave, valor in dicionario_legal.items():
    if valor >= item_majoritario:
        print(chave)