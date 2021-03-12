#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
#e mostreo comprimento da hipotenusa

#Blioteca
from math import hypot

#Entrada de dados
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))

#Manipulação de dados
h = hypot(co, ca)

#Saída de dados
print('Hipotenusa de {} e {} é {:.2f}'.format(co, ca, h))

#END