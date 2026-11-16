#dado um array meu_arrayzao contendo n números distindos no intervalo [0, n]
#retorne o único número no intervalo que está faltando no array

meu_arrayzao = [0,1,3,4,5]

tamanho_meu_arrayzao = len(meu_arrayzao)
soma_valor_meu_arrayzao = sum(meu_arrayzao)

soma_total = tamanho_meu_arrayzao * (tamanho_meu_arrayzao + 1) // 2

print(soma_total - soma_valor_meu_arrayzao)