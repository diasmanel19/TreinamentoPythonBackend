# dado um array de numero inteiros, retorne quantos deles contêm um número par de digitos
# nums = [12,345,2,6,7896]

numero = [12,345,2,6,7896]

contador = 0

for i in numero:
    quantidade = (len(str(i)))
    if quantidade % 2 == 0:
        contador += 1

print(contador)
