#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

dias = int(input('Informe a quantidade de dias: '))
km = float(input('Informe a quantidade de km rodados: '))

dias = 60 * dias
km = km * 0.15

print('Valor a pagar: R${:.2f}'.format(dias+km))
