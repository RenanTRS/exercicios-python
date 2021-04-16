#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da 
#estrutura na tela.

student = {}
student['nome'] = str(input("Student's name: ")).strip().title().split()[0]
student['average'] = float(input("Student's average: "))

#if logic
if student['average'] <= 5:
    student['situation'] = 'Disapproved'
else:
    student['situation'] = 'Approved'

#for logic
for k, v in student.items():
    print(f'{k} is equal to {v}')
