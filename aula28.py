#dado um arrayz de numeros inteiros, cada elemento aparece duas vezes, exceto um. Encontre aquele unico
from operator import xor

numeros = [4, 1, 2, 1, 2]

unico = 0

for numero in numeros:
    unico ^= numero

print(unico)