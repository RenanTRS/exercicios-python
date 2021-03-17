#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a segunga reta: '))
r3 = float(input('Informe a terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Estas retas formam um triângulo.')
else:
    print('Estas retas não formam um triângulo')
