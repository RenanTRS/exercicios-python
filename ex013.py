#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input('Informe o seu salário: R$'))

au =  (sal * 15)/100

print('Seu novo salário com o aumento de 15% é R${:.2f}'.format(sal+au))