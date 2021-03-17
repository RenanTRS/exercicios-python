#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por cada km acima do limite

vel = int(input('Digite a velocidade do carro em Km: '))

if vel > 80:
    multa = (vel - 80)*7
    print('Excesso de velocidade! Multa de R${},00'.format(multa))
else:
    print('{}km, dentro do limite de velocidade'.format(vel))
