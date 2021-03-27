#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

qtd = int(input('Digite a quantidade de termos: '))
cont = 3
t1 = 0
t2 = 1

print('{} -> {} -> '.format(t1, t2), end='')
while cont <= qtd:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

print('Fim')