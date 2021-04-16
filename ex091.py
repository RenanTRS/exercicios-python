#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#library
from random import randint

#for logic
for c in range(0, 4):
    print(randint(1, 6))