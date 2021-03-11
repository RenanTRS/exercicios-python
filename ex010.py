#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

dol = 5.55 #11/03/21 ÊÊÊÊÊ Brasil kkkk
carteira = float(input('Digite quantos reais $$$ você tem na carteira: R$'))

facada = carteira / dol
print('R${:.2f} compram ${:.2f}'.format(carteira, facada))