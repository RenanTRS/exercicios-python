#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
#sua categoria, de acordo com a idade: Até 9 anos mirim. Até 14 anos infantil. Até 19 anos junior. Até 25 
#anos sênior. acima master

from datetime import date
anoAtual = date.today().year

anonasc = int(input('Ano em que o atleta nasceu: '))
idade = anoAtual - anonasc

if idade <= 9:
    print('{} anos. Categoria mirim.'.format(idade))
elif idade <= 14:
    print('{} anos. Categoria infantil.'.format(idade))
elif idade <= 19:
    print('{} anos. Categoria junior'.format(idade))
elif idade <= 25:
    print('{} anos. Categoria sênior.'.format(idade))
else:
    print('{} anos. Categoria master.'.format(idade))

#END