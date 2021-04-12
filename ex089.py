#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim 
#contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

#variables
studentsList = []
student = []

#while logic
while True:
    student.append(str(input('Name: ')).strip().title())
    student.append(float(input('Grade 1: ')))
    student.append(float(input('Grade 2: ')))
    studentsList.append(student[:])
    student.clear()
    #flag
    opc = str(input('Do you want to continue [Y/N]: ')).strip().lower()
    if 'n' in opc:
        break

print(studentsList)
