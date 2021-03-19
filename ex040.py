#Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final, 
#de acordo com a média atingida: Média abaixo de 5.0: Reprovado. Média entre 5.0 e 6.9: Recuperação. 
#Média 7.0 ou superior: Aprovado

from time import sleep
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2 #pegando média das notas


print('PROCESSANDO....')
sleep(1) #atraso dramático

if media < 5:
    print('\033[1mHAHAHAHAHAH')
    sleep(1)
    print('Ai, ai, assim vocês me matam HAHAHAHAHA')
    sleep (1)
    print('Alguém vai dormir com o bumbum dolorido hoje')
    print('Média: \033[31m{}\033[m\033[1m Quero só ver o que vai ser na próxima. Boa noite e bons sonhos, cê vai precisar ;)'.format(media))
elif media >= 5 and media < 7:
    print('\033[1mNa traaaaaaaaaaave!!!')
    print('Pelo visto vamos nos ver mais vezes hein, já vou logo avisando que sou comprometido.')
    print('Média: \033[33m{}'.format(media))
else:
    print('\033[1mTem nem o que falar, passou, vai pela sombra')
    print('Média: \033[32m{}'.format(media))
