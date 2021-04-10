#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os 
#valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numberList = []
pair = []
odd = []

for c in range(1, 8):
    number = int(input(f'Enter the {c}º number: '))
    numberList.append(number)
    if number % 2 == 0:
        pair.append(number)
    else:
        odd.append(number)

pair.sort()
odd.sort()
#print(numberList)
print(f'Pair numbers: {pair}')
print(f'Odd numbers: {odd}')
