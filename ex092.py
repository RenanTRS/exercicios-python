#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a
#CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
#com quantos anos a pessoa vai se aposentar.

#library
from datetime import date

#variables
register = {}
currentYear = date.today().year

name = str(input('Name: ')).strip().title().split()[0]
register['name'] = name
year = int(input('Year of Birth: '))
age = currentYear - year
register['age'] = age
workCard = int(input('Work permit: '))
register['workCard'] = workCard

#if logic
if workCard != 0:
    yearHiring = int(input('Year of Hiring: '))
    register['yearHiring'] = yearHiring
    pay = float(input('Pay: $'))
    register['pay'] = pay

#Code exit
print(register)
#End