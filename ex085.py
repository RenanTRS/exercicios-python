#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os 
#valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#variable
numberList = [[], []]

#for logic
for c in range(1, 8):
    number = int(input(f'Enter the {c}º number: '))
    if number % 2 == 0:
        numberList[0].append(number)
    else:
        numberList[1].append(number)

numberList[0].sort()
numberList[1].sort()

#code exit
print(f'Pair numbers: {numberList[0]}')
print(f'Odd numbers: {numberList[1]}')
