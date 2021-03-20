#Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep

n = randint(1, 3)#Escolha da cpu

#Cabeçalho
print('-=-'*20)
print('{:^60}'.format('JOKENPÔ'))
print('-=-'*20)

print('Escolha sua opção:')
print('[1] - PEDRA\n[2] - PAPEL\n[3] - TESOURA')
opc = int(input('Sua jogada: '))

#Validar dado-----------------------------
if opc > 3:
    print('Opção inválida!')
elif opc <=3:  
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)

#Condição e saída----------------------------------
if opc == 1:#Se pedra
    if n == 1:
        print('-'*20)
        print('{:^20}'.format('PEDRA x PEDRA'))
        print('-'*20)
        print('\033[1;33mEmpate')

    elif n == 2:
        print('-'*20)
        print('{:^20}'.format('PEDRA x PAPEL'))
        print('-'*20)
        print('\033[1;31mVocê Perdeu')

    elif n == 3:
        print('-'*20)
        print('{:^20}'.format('PEDRA x TESOURA'))
        print('-'*20)
        print('\033[1;32mVocê Venceu')

elif opc == 2:#Se papel
    if n == 1:
        print('-'*20)
        print('{:^20}'.format('PAPEL x PEDRA'))
        print('-'*20)
        print('\033[1;32mVocê Venceu')
    
    elif n == 2:
        print('-'*20)
        print('{:^20}'.format('PAPEL x PAPEL'))
        print('-'*20)
        print('\033[1;33mEmpate')
    
    elif n == 3:
        print('-'*20)
        print('{:^20}'.format('PAPEL x TESOURA'))
        print('-'*20)
        print('\033[1;31mVocê Perdeu')

elif opc == 3:#Se tesoura
    if n == 1:
        print('-'*20)
        print('{:^20}'.format('TESOURA x PEDRA'))
        print('-'*20)
        print('\033[1;31mVocê Perdeu')
    
    elif n == 2:
        print('-'*20)
        print('{:^20}'.format('TESOURA x PAPEL'))
        print('-'*20)
        print('\033[1;32mVocê Venceu')
    
    elif n == 3:
        print('-'*20)
        print('{:^20}'.format('TESOURA x TESOURA'))
        print('-'*20)
        print('\033[1;33mEmpate')

#END