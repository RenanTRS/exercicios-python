#O mesmo professor do desafio anteriro quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

#Biblioteca
from random import shuffle

#Entrada de dados
n1 = str(input('Aluno: '))
n2 = str(input('Aluno: '))
n3 = str(input('Aluno: '))
n4 = str(input('Aluno: '))
ordem = [n1, n2, n3, n4]

#Manipulação de dados
shuffle(ordem)

#Saída de dados
print(ordem)

#END