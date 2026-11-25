# Resolução de problemas - Parte 22
# Retorne a media de todos os salarios, com exceção do maior e menor

salario = [3847, 1936, 6284, 2571]

organizacao_de_salario = sorted(salario)

total = 0

for i in organizacao_de_salario:
    if i != min(organizacao_de_salario) and i != max(organizacao_de_salario):
        total += i

print(total // len(organizacao_de_salario))