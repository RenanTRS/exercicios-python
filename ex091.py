#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#library
from random import randint

#variable
rank = {}
game = {'player1': randint(1, 6), 'player2': randint(1, 6), 'player3': randint(1, 6), 'player4': randint(1, 6)}
print(game)