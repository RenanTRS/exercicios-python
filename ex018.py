#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

#Blibliotecas
from math import radians, sin, cos, tan

#Entrada de dados
a = int(input('Informe o ângulo: '))

#Manipulação de dados
seno = sin(radians(a))
coss = cos(radians(a))
tang = tan(radians(a))

#Saída de dados
print('O seno de {} é {:.2f}'.format(a, seno))
print('O cosseno de {} é {:.2f}'.format(a, coss))
print('A tangente de {} é {:.2f}'.format(a, tang))

#END