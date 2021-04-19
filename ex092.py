#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a
#CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
#com quantos anos a pessoa vai se aposentar.

#library
from datetime import date

#variables
register = {}
#currentYear = date.today().year

register['name'] = str(input('Name: ')).strip().title().split()[0]
year = int(input('Year of Birth: '))
register['age'] = date.today().year - year
register['workCard'] = int(input('Work permit: '))

#if logic
if register['workCard'] != 0:
    register['yearHiring'] = int(input('Year of Hiring: '))
    register['pay'] = float(input('Pay: $'))
    retirement = register['yearHiring'] - year
    register['retirement'] = retirement + 35

#Code exit
print('==' * 20)

#for logic
for k, v in register.items():
    print(f'The {k} is {v}')

#End