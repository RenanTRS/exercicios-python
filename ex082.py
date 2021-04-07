#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os
#valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

#Variables
pair = []
odd = []
values = []

while True:
    number = int(input('Enter a number: '))
    values.append(number)
    opc = input('Do you want to continue [Y/N]: ').strip().lower()
    if 'n' in opc:
        break

print(values)
