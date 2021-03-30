#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado 
#(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. #OBS: considere que o caixa possui 
#cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Digite o valor que você quer sacar R$'))
total = valor
cedulas = 50
totalCedulas = 0

while True:
    if total >= cedulas:
        total -= cedulas
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Foram usadas {totalCedulas} notas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalCedulas = 0
        if total == 0:
            break
