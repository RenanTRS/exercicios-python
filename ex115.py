#Vamos criar um menu em Python, usando modularização.

def menu(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)

while True:
    menu('Menu Principal')
    print(f'\033[1;33m1 -\033[1;34m Ver pessoas cadastradas\033[m')
    print(f'\033[1;33m2 -\033[1;34m Cadastrar nova pessoa\033[m')
    print(f'\033[1;33m3 -\033[1;34m Sair do Sistema\033[m')

    opc = int(input('Sua Opção: '))
    if opc == 3: #flag
        print(f'Saindo do sistema')
        break
    else:
        print(f'{opc}')