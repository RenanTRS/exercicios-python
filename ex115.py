#Vamos criar um menu em Python, usando modularização.

from time import sleep

def menu(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

while True:
    menu('Menu Principal')
    print(f'\033[1;33m1 -\033[1;34m Ver pessoas cadastradas\033[m')
    print(f'\033[1;33m2 -\033[1;34m Cadastrar nova pessoa\033[m')
    print(f'\033[1;33m3 -\033[1;34m Sair do Sistema\033[m')

    try:
        opc = int(input('\033[1;32mSua Opção: \033[m'))
    except (ValueError):
        print(f'\033[1;31mErro: por favor, digite um número inteiro válido.\033[m')
    
    else:
        if opc == 3: #flag
            print(f'Saindo do sistema')
            break
        else:
            if opc == 1:
                menu('Opção 1')
                sleep(1)
            elif opc == 2:
                menu('Opção 2')
                sleep(1)