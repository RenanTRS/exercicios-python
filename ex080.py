#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
#(sem usar o sort()). No final, mostre a lista ordenada na tela.

numberList = []
cont = bigger = smaller = value = 0
for c in range(0, 5):
    value = int(input('Enter a number: '))
    if c == 0 or value > numberList[len(numberList)-1]:
        numberList.append(value)
    else:
        while True:
            if value < numberList[cont]:
                numberList.insert(cont, value)
            cont += 1

print(numberList)