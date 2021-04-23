#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas 
#ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato.

#function
def equals():
    print('=='* 20)

player = {}
goals = []
total = 0

#inputs
player['name'] = str(input('Name: ')).strip().title().split()[0]
qtd = int(input(f"How many matches {player['name']} played: ")) #matches

#for logic
for c in range(0, qtd):
    goals.append(int(input(f'How many goals in game {c+1}: ')))
    total += goals[c]

player['goals'] = goals[:]
player['total'] = total

#code exit
equals()
print(player)
equals()

#for exit logic
for k, v in player.items():
    print(f'The {k} field has a value of {v}.')
equals()

print(f'The player {player["name"]} played {qtd} matches.')
#for exit logic
for pos, c in enumerate(player['goals']):
    print(f' => In matches {pos+1}, he scored {c} goals.')
print(f'Total: {player["total"]} goals.')
#End