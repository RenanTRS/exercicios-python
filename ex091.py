#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#library
from random import randint

#variable
rank = []
#for logic
for c in range(0, 4):
    number = randint(1, 6)
    print(number)
    #if logic
    if c == 0:
        rank.append(number)
    else:
        for pos, i in enumerate(rank):
            if i < number:
                rank.insert(pos, number)

print(rank)