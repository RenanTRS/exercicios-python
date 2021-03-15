#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

#Entrada de dados---------------------------------------------
nome = str(input('Digite o seu nome completo: ')).strip().title()

while nome == '':
    nome = str(input('Digite o seuno nome completo: ')).strip().title()

#Manipulação de dados----------------------------------
name = nome.split()

#Saída de dados-----------------------------------------
print('Primeiro nome: {}'.format(name[0]))
print('Último nome: {}'.format(name[len(name)-1]))

#END