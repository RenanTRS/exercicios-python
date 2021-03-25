#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
#até ter um valor correto.

sexo = str(input('Digite o sexo: [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[1;31mValor inválido\033[m Digite o sexo: [M/F]: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso.'.format(sexo))
