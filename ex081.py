#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

number = []
while True:
    number.append(int(input('Enter a number: ')))
    opc = input('Do you want to continue [Y/N]: ').strip().lower()
    if 'n' in opc:
        break

print(number)
