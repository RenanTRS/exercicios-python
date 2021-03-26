#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
#até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

flag = randint(0, 10)
num = int(input('Tente advinha um número entre 0 e 10: '))

if num == flag:
    print('\033[1;32mO miserável é um gênio.\033[m')
else:
    while num != flag:
        num = int(input('\033[1;31mErrooooou\033[m Tente Novamente: '))
        if num == flag:
            print('Acertou Miseravi')
    
print('Fim')