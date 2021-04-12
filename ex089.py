#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim 
#contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

#variables
studentsList = []
student = []

#while logic
while True:
    student.append(str(input('Name: ')).strip().title().split()[0])
    student.append(float(input('Grade 1: ')))
    student.append(float(input('Grade 2: ')))
    studentsList.append(student[:])
    student.clear()
    #flag
    opc = str(input('Do you want to continue [Y/N]: ')).strip().lower()
    if 'n' in opc:
        break
#code exit
print('==' * 20)
print('Nº Name   Grade Point')
#for logic
for pos, c in enumerate(studentsList):
    print(f'{pos}  {c[0]:<5} {(c[1]+c[2])/2:>8}')

while True:
    #second flag
    number = int(input("Show me the student's situation (999 break): "))
    if number == 999:
        break
    else:
        for pos, s in enumerate(studentsList):
            if number == pos:
                print(f'Student: {s[0]} | Grades: {s[1]}, {s[2]}')
