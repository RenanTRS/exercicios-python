def linha():
    print('-'*42)

def cabecalho(msg, tam=42):
    linha()
    print(msg.center(tam))#Centraliza na quantidade px que foi passada
    linha()

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro: por favor digite um valor inteiro válido\033[m')
        except(KeyboardInterrupt):
            print(f'\033[1;31mEntrada de dados interrompida pelo usuário\033[m')
        else:
            return n

def menu(lista):
    cont = 1
    for c in lista:
        print(f'\033[1;33m{cont} -\033[1;34m {c}\033[m')
        cont += 1
    linha()
    opc = leiaInt('\033[1;32mSua opção: \033[m')
    return opc