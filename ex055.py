#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = 0

for p in range(0, 5):
    peso = float(input('Informe o peso da {}º pessoa: '.format(p+1)))
