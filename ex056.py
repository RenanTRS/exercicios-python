#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho. 
#Quantas mulheres têm menos de 20 anos.

maior = mediaIdade = qtdM = 0

for c in range(0, 4):
    print('----{}ºPESSOA----'.format(c+1))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().title()[0] #Recorte da primeira letra.
    mediaIdade += idade

    if sexo == 'M' and c == 0:
        maior = idade
        nomeVelho = nome
    elif sexo == 'M' and idade > maior:
        maior = idade
        nomeVelho = nome
    
    if sexo == 'F' and idade < 20:
        qtdM += 1

mediaIdade = mediaIdade /4

print('Média de idade do grupo: {}'.format(mediaIdade))
print('O homem mais velho é o {}, ele tem {} anos'.format(nomeVelho, maior))
print('{} mulheres têm mais de 20 anos'.format(qtdM))
