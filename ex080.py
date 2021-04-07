#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
#(sem usar o sort()). No final, mostre a lista ordenada na tela.

numberList = []
cont = bigger = smaller = value = 0
for c in range(0, 5):
    value = int(input('Enter a number: '))
    if cont == 0:
        numberList.append(value)
    else:
        for y in numberList:
            
    cont