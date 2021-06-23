from interface import *
from time import sleep

while True:
    cabecalho('Menu Principal')
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opc == 1:
        cabecalho('Opção 1')
        sleep(.5)
    elif opc == 2:
        cabecalho('Opção 2')
        sleep(.5)
    elif opc == 3: #flag
        cabecalho('Saindo do sistema, até logo!')
        sleep(1)
        break
    else:
        print(f'\033[1;31mErro: Digite uma opção válida.\033[m')
        sleep(1)
        
