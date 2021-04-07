#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


#Variables
number = []

#list logic
while True:
    number.append(int(input('Enter a number: ')))
    opc = input('Do you want to continue [Y/N]: ').strip().lower()
    if 'n' in opc:
        break

#code exit
print(f'Numbers entered {len(number)}')
number.sort(reverse=True)
print(f'Decending list: {number}')
if 5 in number:
    print('The value 5 was entered.')
else:
    print('The value 5 was not entered.')
