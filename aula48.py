#Resolução de problemas - Parte 20
# Dada uma string s que consiste em palavras e espaços, retorne o comprimento da última palavra da string.

s = "   O         Palmeiras vai          ganhar            a      Libertadores            "

meu_array = s.split()

print(len(meu_array[-1]))