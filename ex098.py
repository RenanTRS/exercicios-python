#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que 
#realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep
#functions
def breakLine():
    print('')
    print('=-'*20)
def contador(a, b, c):
    if c > 0:
        print(f'Count from {a} to {b} of {c} in {c}')
        for i in range(a, b+1, c):
            print(i, end=' ', flush=True)
            sleep(0.5)
        breakLine()
    else:
        print(f'Count from {a} to {b} of {c*-1} in {c*-1}')
        for i in range(a, b-1, c):
            print(i, end=' ', flush=True) 
            sleep(0.5)
        breakLine()

print('Count from 1 to 10 of 1 in 1:')
for c in range(1, 11):
    print(c, end=' ', flush=True)
    sleep(0.5)
breakLine()

print('Cont from 10 to 0 of 2 in 2:')
for c in range(10, -1, -2):
    print(c, end=' ', flush=True)
    sleep(0.5)
breakLine()

print('Now it is your turn to customize the count')
begin = int(input('Begin: '))
finish = int(input('Finish: '))
step = int(input('Step: '))
breakLine()

contador(begin, finish, step)