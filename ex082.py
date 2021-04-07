#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os
#valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

#Variables
pair = []
odd = []
values = []

#list logic
while True:
    number = int(input('Enter a number: '))
    values.append(number)
    if number % 2 == 0:
        pair.append(number)
    else:
        odd.append(number)
    opc = input('Do you want to continue [Y/N]: ').strip().lower()
    if 'n' in opc:
        break

#code exit
print(f'Full list:{values}')
print(f'Full pairs list:{pair}')
print(f'Full odd list: {odd}')
