#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite um último número: '))

numeros = (n1, n2, n3, n4)
print(f'O número 9 apareceu: {numeros.count(9)} vezes')
if numeros.count(3) > 0:
    print(f'O número 3 na posição: {numeros.index(3)+1}')
else:
    print(f'Não possui valor 3')
print('Valores pares digitados: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')

print('')