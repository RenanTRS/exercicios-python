#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#library
from random import randint
from operator import itemgetter

#variable
rank = {}
game = {'player1': randint(1, 6), 'player2': randint(1, 6), 'player3': randint(1, 6), 'player4': randint(1, 6)}
#for logic
for k, v in game.items():
    print(f'{k} scored {v} in the dice.')
rank = sorted(game.items(), key=itemgetter(1), reverse=True)
print(game)
print(rank)
