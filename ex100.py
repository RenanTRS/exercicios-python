#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 
#5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela 
#função anterior.

from random import randint
def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 9))
    
def somaPar(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(soma)

numeros = []
sorteia()
print(f'Sorteando 5 valores da lista:', end=' ')
for c in numeros:
    print(c, end=' ')
print('') #breakLine
print(f'Somando os valores pares de {numeros}:', end=' ')
somaPar(numeros)