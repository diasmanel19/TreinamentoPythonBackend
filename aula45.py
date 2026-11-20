# Resolução de problemas - Parte 17
# Dado um número inteiro não negativo x, retorne a raiz quadrada de x arredondada para o numero inteiro mais próximo.
# O número inteiro retornado também deve ser não negativo

import math

x = int(input("digite um número para obter ele ao quadrado:" ))

resultado = math.sqrt(x)

print(math.trunc(resultado))