#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho. 
#Quantas mulheres têm menos de 20 anos.

for c in range(0, 4):
    print('----{}ºPESSOA----'.format(c+1))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().title()[0] #Recorte da primeira letra.
    