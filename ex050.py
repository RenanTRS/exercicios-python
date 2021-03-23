#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se  valor digitado for 
#ímpar desconsidereo.
s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n

print('soma dos valores pares: {}'.format(s))