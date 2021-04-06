#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá 
#dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
number = []
value = 0
while True:
    value = int(input('Enter a number: '))
    if value not in number:
        number.append(value)
    else:
        print(f'The number {value} already exists')
    opc = str(input('Do you wish to continue [Y/N]: ')).strip().lower()
    if 'n' in opc:
        break
number.sort()
print(number)