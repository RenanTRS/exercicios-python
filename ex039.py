#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda 
#vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

anoAtual = date.today().year #pegando o ano na máquina do usuáiro.
nasc = int(input('Ano de nascimento do infleiz: '))

alist = anoAtual - nasc

if alist < 18:
    tempo = 18 - alist
    print('Calma, faltam \033[1;33m{}\033[m anos para o seu sofrimento. hehe'.format(tempo))
elif alist == 18:
    print('\033[1;31mWellcome to the hell baby. hahaha\033[m')
elif alist > 18:
    tempo = alist - 18
    print('Olha só quem sobreviveu... Quem diria, já fazem {} anos'.format(tempo))
 