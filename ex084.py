#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

#variables
peopleList = []
person = []
weight = []
bigger = smaller = 0

#while logic
while True:
    person.append(str(input('Name: ')).strip().title())
    person.append(float(input('Weight: ')))
    peopleList.append(person[:])
    person.clear()
    opc = str(input('Do you want to continue [Y/N]: ')).strip().lower()
    if 'n' in opc:
        break

print(peopleList)
