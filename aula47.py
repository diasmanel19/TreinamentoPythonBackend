# Resolução de problemas - Parte 19
# Definimos o uso de letras maiúsculas em uma palavra como correto quando o seguinte caso é válido:
# Todas as letras desta palavra são maiúscula, como "EUA"
# Dada uma palavra de string, retorne True se o uso de letras maiúsculas está correto.

array_nomes = ["Melancia", "AVESTRUZ", "ESpELho"]

contador = 0

for i in array_nomes:
    if i.isupper():
        contador += 1
        print(f"{i}: está em maiúsculas")
    else:
        print(f"{i}: não está toda em maiúsculas")

print(f"Total em maiúsculas: {contador}")

if contador == len(array_nomes):
    print("Todas estão corretas!")
else:
    print("Nem todas estão corretas!")


