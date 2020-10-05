aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Agora informe a nota da primeira avaliação: '))
nota2 = float(input('Agora informe a nota da segunda avaliação: '))
media = (nota1 + nota2) / 2

print()
print('Media: ', media)

if media < 7:
    print('O Aluno foi reprovado!')
else:
    print('Parabéns {}, você foi aprovado(a)'.format(aluno))
