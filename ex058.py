#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
#até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

cont = 1
flag = randint(0, 10)
num = int(input('Tente advinha um número entre 0 e 10: '))

if num == flag:
    print('\033[1;32mO miserável é um gênio.\033[m')
else:
    while num != flag:
        cont += 1
        if num < flag:
            print('\033[1;31mErrooooou! É mais\033[m')
        else:
            print('\033[1;31mErroooooo! É Menos\033[m')
        num = int(input('Tente Novamente: '))
        if num == flag:
            print('\033[1;32mAcertou Miseravi\033[m')
            print('Tentativas: {}'.format(cont))
    
#END