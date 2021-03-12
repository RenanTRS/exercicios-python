#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.

#Biblioteca
from random import choice

#Entrada de dados
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))

#Manipulação de dados
l = [n1, n2, n3, n4]
condenado = choice(l)

#Saída de dados
print('O condenado de hoje foi: {}'.format(condenado))

#END