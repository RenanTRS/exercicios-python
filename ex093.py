#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas 
#ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato.

player = {}
player['name'] = str(input('Name: ')).strip().title().split()[0]
player['qtd'] = int(input(f"How many matches did {player['name']} play: "))
print(player['name'])
print(player['qtd'])
