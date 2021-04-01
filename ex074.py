#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
#e também indique o menor e o maior valor que estão na tupla.

from random import randint
maior = menor = cont = 0

numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

print(numeros)
print(f'O maior valor sorteado: {max(numeros)}')
print(f'O menor valor sorteado: {min(numeros)}')