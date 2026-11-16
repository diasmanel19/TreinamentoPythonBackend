#receber uma lista de palavras e organizar em ordem alfabetica

palavras = []

for i in range(5):
    palavras.append(input())

palavras.sort()

print(palavras)