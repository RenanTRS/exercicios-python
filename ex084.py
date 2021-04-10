#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

#variables
peopleList = []
person = []
#weight = []
bigger = []
smaller = []
count = 0

#while logic
while True:
    person.append(str(input('Name: ')).strip().title())
    person.append(float(input('Weight: ')))
    peopleList.append(person[:])
    
    if count == 0:
        bigger.append(person[:])
        smaller.append(person[:])
    
    else:
        if bigger[0][1] < person[1]:
            bigger = person[:]
        elif bigger[0][1] == person[1]:
            bigger.append(person[:])
        if smaller[0][1] > person[1]:
            smaller = person[:]
        elif smaller[0][1] == person[1]:
            smaller.append(person[:])

    person.clear()
    count += 1

    #flag
    opc = str(input('Do you want to continue [Y/N]: ')).strip().lower()
    if 'n' in opc:
        break

#code exit
print(f'Number of people regitered: {len(peopleList)}')
#print(f'The biggest weight was {bigger[0][1]}kg, Name: {bigger[0][0]}')
print(bigger)
#print(f'The lowest weight was: {smaller[0][1]}kg, Name: {smaller[0][0]}')
print(smaller)
