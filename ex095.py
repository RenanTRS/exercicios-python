#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do 
#aproveitamento de cada jogador.

#Functions-------------------
def equals():
    print('=='*30)

#Inputs----------------------
player = {}
goals = []
totalGoals = 0

player['name'] = str(input('Name: ')).strip().title().split()[0]
qtd = int(input(f'How many matches {player["name"]} played: '))

#for logic-------------------
for c in range(0 < qtd):
    goals.append(int(input(f'How many goals in game {c+1}: ')))
    totalGoals += goals[c]

#----------------------------
player['goals'] = goals[:]
player['total'] = totalGoals