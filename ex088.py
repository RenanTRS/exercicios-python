#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai 
#sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#library
from random import randint

game = int(input('How many games do you want? '))
numberList = []
count = 0

for c in range(0, game):
    print(f'Game {c+1}: ', end='')
    for n in range(0, 6):
        while True:
            number = randint(1, 60)
            if number not in numberList:
                numberList.append(number)
                break
    
    numberList.sort()
    print(numberList)
    numberList.clear()