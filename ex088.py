#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai 
#sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#library
from random import randint

#variables
game = int(input('How many games do you want? '))
numbers = []
numberList = []
count = 0
#for logic
for c in range(0, game):
    for n in range(0, 6):
        #while logic
        while True:
            number = randint(1, 60)
            if number not in numbers:
                numbers.append(number)
                break
    #data manipulation
    numbers.sort()
    numberList.append(numbers[:])
    numbers.clear()
#code exit
#print(numberList)
for pos, g in enumerate(numberList):
    print(f'Game {pos+1}: {g}')
