#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

#variables
peopleList = []
person = []
weight = []
bigger = []
smaller = []
count = 0

#while logic
while True:
    person.append(str(input('Name: ')).strip().title())
    person.append(float(input('Weight: ')))
    peopleList.append(person[:])
    
    if count == 0:
        bigger = person[:]
        smaller = person[:]
    else:
        if bigger[1] < person[1]:
            bigger = person[:]
        elif bigger[1] == person[1]:
            bigger.append(person[:])
        if smaller[1] > person[1]:
            smaller = person[:]
        elif smaller[1] == person[1]:
            smaller.append(person[:])
    
    person.clear()
    count += 1
    
    #flag
    opc = str(input('Do you want to continue [Y/N]: ')).strip().lower()
    if 'n' in opc:
        break

#code exit
print(peopleList)
print(len(peopleList))
print(bigger)
print(smaller)
