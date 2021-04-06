#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado 
#e as suas respectivas posições na lista.

numberList = []
bigger = pBigger = smaller = pSmaller = 0

for c in range(0, 5):
    numberList.append(int(input('Enter a number: ')))

for pos, y in enumerate(numberList):
    if pos == 0:
        bigger = smaller = y
        pBigger = pSmaller = pos
    else:
        if bigger < y:
            bigger = y
            pBigger = pos
        if smaller > y:
            smaller = y
            pSmaller = pos

print(f'Highest value: {bigger} in position:{pBigger + 1}')
print(f'Lowest value: {smaller} in position:{pSmaller + 1}')
