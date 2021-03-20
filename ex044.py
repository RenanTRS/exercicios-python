#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
#de pagamento: 
#À vista dinheiro/cheque: 10% de desconto. 
#À vista no cartão: 5% de desconto. 
#Em até 2x no cartão: preço normal. 
#3x ou mais no cartão: 20% de juros.

valor  = float(input('Valor a ser pago: R$'))
print('Formas de pagamento')
print('[1] - À vista dinherio/cheque com 10%  de desconto.\n[2] - À vista no cartão com 5% de desconto.\n[3] - Cartão 2x sem juros.\n[4] - Cartão 3x ou mais com 20% de juros')
opc = int(input('Opção: '))

if opc == 1:
    total = valor - ((valor * 10)/100)

elif opc == 2:
    total = valor - ((valor * 5)/100)

elif opc == 3:
    total = valor
    print('Compra parcelada em 2x de R${:.2f}'.format(valor / 2))

elif opc == 4:
    total = valor + ((valor * 20)/100)
    #nvalor = total
    qtd = int(input('Quantas parcelas: '))
    print('Compra parcelada em {}x de R${:.2f}'.format(qtd, total / qtd))

print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, total))

#END