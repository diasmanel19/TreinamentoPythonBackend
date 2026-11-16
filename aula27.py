# Você recebe um array de números inteiros meu_arrayzinho.
# Os elementos únicos de um array são os elementos que aparecem exatamente uma vez no array.
# Retorne a soma de todos os elementos únicos de meu_arrayzinho.

#parte 1 
meu_array = [7, 3, 9, 3, 12, 5, 7, 8, 12, 4, 15, 5, 10]


#parte 2 
from collections import Counter

conta = Counter(meu_array)

#parte 3 
soma = 0

for numero in conta:
    if conta[numero] == 1:
        soma += numero
    

print(soma)