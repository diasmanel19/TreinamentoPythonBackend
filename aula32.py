# dado um array de inteiros meu_array, um inteiro sortudo é um inteiro que tem uma frequência no array igual ao seu valor

meu_array = [2, 2, 3, 3, 3, 4]

from collections import Counter

sortudo = Counter(meu_array)

for numero in meu_array:
    if sortudo[numero] == numero:
        print("sortudo")
    else:
        print("azarado")