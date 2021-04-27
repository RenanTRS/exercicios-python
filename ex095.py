#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do 
#aproveitamento de cada jogador.

#Functions-------------------
def equals():
    print('=='*30)
def trace():
    print('-'*30)
def breakLine():
    print('')

#Inputs----------------------
player = {}
players = []
goals = []
totalGoals = 0

#while logic-----------------
while True:
    player['name'] = str(input('Name: ')).strip().title().split()[0]
    qtd = int(input(f'How many matches {player["name"]} played: '))

    #for logic-------------------
    for c in range(0, qtd):
        #print(c)
        goals.append(int(input(f'How many goals in game {c+1}: ')))
        totalGoals += goals[c]

    #----------------------------
    player['goals'] = goals[:]
    player['total'] = totalGoals
    players.append(player.copy())
    
    #flag------------------------
    opt = str(input('Do you want to continue [Y/N]: ')).strip().upper().split()[0]
    #if logic
    if 'N' in opt:
        break

#exit------------------------
print(players)