#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
#Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

timesBrasileirao = ('Corinthians', 'Flamento', 'São Paulo', 'Palmeiras', 'Bota Fogo', 'Santos', 'Grêmio', 'Chapecoense', 'Ponte Preta', 'Atlético', 'Inter', 'Bahia', 'Fluminense', 'Cruzeiro', 'Vasco', 'Ceará', 'Vitória', 'Paraná', 'Atlético-Mg', 'Atletico-Go')
print(timesBrasileirao[:5])
print(timesBrasileirao[len(timesBrasileirao)-4:])
print(sorted(timesBrasileirao))
print(timesBrasileirao.index('Chapecoense'))