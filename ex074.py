#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
#e também indique o menor e o maior valor que estão na tupla.

from random import randint
maior = menor = cont = 0

numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
for c in numeros:
    if cont == 0:
        maior = menor = c
    else:
        if maior > c:
            maior = c
        if menor < c:
            menor = c

