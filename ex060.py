#Faça um programa que leia um número qualquer e mostre o seu fatorial Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120.

num = int(input('Digite um número: '))
fatorial = num

print('{}!'.format(num), end=' ')
while num > 0:
    if num > 1:
        print('{} x '.format(num), end='')
        fatorial *= num-1
        num -= 1
    else:
        print('{} = '.format(num), end='')
        fatorial *= num
        num -= 1

print(fatorial)