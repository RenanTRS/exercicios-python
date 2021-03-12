#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
#Ex: Digite um número: 6.127, o número 6.127 a parte inteira é 6

#Bibliotecas
from math import trunc

#Entrada de dados
n = float(input('Digite um número real: '))

#Manipulação de dados
nr = trunc(n)

#Saída de dados
print('Número: {}, sua parte inteira: {}'.format(n, nr))

#END