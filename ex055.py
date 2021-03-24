#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = 0

for p in range(0, 5):
    peso = float(input('Informe o peso da {}º pessoa: '.format(p+1)))
    if p == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    
print('Menor peso: {:.2f}'.format(menor))
print('Maior peso: {:.2f}'.format(maior))
