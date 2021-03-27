#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de
#vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint
while True:
    cpu = randint(0, 5)
    j1 = int(input('Digite um número entre 0 e 5: '))
    opc = str(input('Escolha par ou ímpar [I/P]:')).strip().upper()[0]
    soma = j1 + cpu

    if soma % 2 == 0:
        if opc == 'P':
            print(f'P1:{j1} x CPU:{cpu}')
            print(f'{soma} Par, Você ganhou')
        elif opc == 'I':
            print(f'P1:{j1} x CPU:{cpu}')
            print(f'{soma} Par, Você perdeu')
            break
    elif soma % 2 != 0:
        if opc == 'P':
            print(f'P1:{j1} x CPU:{cpu}')
            print(f'{soma} Ímpar, Você perdeu')
            break
        elif opc == 'I':
            print(f'P1:{j1} x CPU:{cpu}')
            print(f'{soma} Ímpar, Você ganhou')