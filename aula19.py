#receber a média do aluno (media >= 6)
print("me diga a sua nota:")

media = float(input())

if media >= 6.0:
    print("Parabéns! Você foi aprovado com sucesso.")
#em recuperação (5 <= media < 6 )
elif media >= 5.0 and media < 6.0:
    print("Opa! Você está de recuperação, estude mais!")
#reprovado (média < 5)
else: 
    print("Você está reprovado!")
