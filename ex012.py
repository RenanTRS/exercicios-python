#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Informe o preço do produto: R$'))

desc = (p * 5)/100

print('O que era antes R${:.2f}, com 5% de desconto fica R${:.2f}'.format(p, p - desc))
