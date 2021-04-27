#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do 
#aproveitamento de cada jogador.

#Functions-------------------
def equals():
    print('=='*30)

#Imputs----------------------
player = {}

player['name'] = str(input('Name: ')).strip().title().split()[0]
qtd = int(input(f'How many matches {player["name"]} played: '))