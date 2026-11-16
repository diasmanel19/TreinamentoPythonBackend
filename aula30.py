# dada uma string s consistindo apenas dos caracteres 'a' e 'b',
# retorne verdadeiro se cada 'a' aparecer antes de cada 'b' na string
# caso contrario, retorne falso

minha_string = 'aaaaab'

if 'ba' not in minha_string:
    print("correto")
else:
    print("incorreto")