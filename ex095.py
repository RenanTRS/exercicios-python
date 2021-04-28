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

#while logic-----------------
while True:
    player['name'] = str(input('Name: ')).strip().title().split()[0]
    qtd = int(input(f'How many matches {player["name"]} played: '))
    totalGoals = 0

    #for logic-------------------
    for c in range(0, qtd):
        #print(c)
        goals.append(int(input(f'How many goals in game {c+1}: ')))
        totalGoals += goals[c]

    #----------------------------
    player['goals'] = goals[:]
    goals.clear()
    player['total'] = totalGoals
    players.append(player.copy())
    
    #flag------------------------
    opt = str(input('Do you want to continue [Y/N]: ')).strip().upper().split()[0]
    #if logic
    if 'N' in opt:
        break

#exit------------------------
equals()
print('cod ', end='')
#for logic-------------------
for i in player.keys():
    print(f'{i:<15}',end='')
breakLine()

#For logic-------------------
for pos, c in enumerate(players):
    print(f'{pos:>4}',end='')
    for d in c.values():
        print(f'{str(d):<15}', end='')
    breakLine()
trace()

#while logic-----------------
while True:
    opt = int(input("Show which player's data: (999 to cancel) "))
    if opt == 999:
        break
    elif opt >= len(players):
        print(f'Error, there is no exist player {opt}')
    else:
        print(f'Player: {players[opt]["name"]}')
        for pos, p in enumerate(players[opt]["goals"]):
            print(f'In matches {pos+1}, he scored {p} goals.')
    trace()