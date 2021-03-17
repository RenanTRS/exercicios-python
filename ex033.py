#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3

print('Maior: {} Menor: {}'.format(maior, menor))