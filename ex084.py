#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

#variables
peopleList = []
person = []
bigger = smaller = count = 0

#while logic
while True:
    person.append(str(input('Name: ')).strip().title())
    person.append(float(input('Weight: ')))
    peopleList.append(person[:])
    
    if count == 0:
        bigger = smaller = person[1]
    
    else:
        if bigger < person[1]:
            bigger = person[1]
        
        if smaller > person[1]:
            smaller = person[1]

    person.clear()
    count += 1

    #flag
    opc = str(input('Do you want to continue [Y/N]: ')).strip().lower()
    if 'n' in opc:
        break

#code exit
print(f'Number of people registered: {len(peopleList)}')
print(f'The biggest weight was {bigger}kg, Name:', end=' ')
for c in peopleList:
    if c[1] == bigger:
        print(f'[{c[0]}]', end=' ')
print('')
print(f'The lowest weight was: {smaller}kg, Name:', end=' ')
for p in peopleList:
    if p[1] == smaller:
        print(f'[{p[0]}]', end=' ')
print('')
