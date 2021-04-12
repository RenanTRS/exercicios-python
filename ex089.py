#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim 
#contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

#variables
studentsList = []
student = []

name = str(input('Name: ')).strip().title()
grade1 = float(input('Grade 1: '))
grade2 = float(input('Grade 2: '))
