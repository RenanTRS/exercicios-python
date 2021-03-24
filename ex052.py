#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
cont = 0

for c in range(1, n+1):
    if n % c == 0:
        cont += 1
        print('\033[32m{}'.format(c), end= ' ')
    else:
        print('\033[31m{}'.format(c), end=' ')

print('\033[m')
if cont == 2:
    print('{} é um número primo'.format(n))
else:
    print('{} não é um número primoe'.format(n))