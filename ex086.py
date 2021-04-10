#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na 
#tela, com a formatação correta.

#variable
blocks = [[0, 0, 0], [0, 0, 0], [0, 0, 0,]]

#for logic
for c in range(0, 3):
    for y in range(0, 3):
        blocks[c][y] = int(input(f'Enter a number for [{c}, {y}]: '))

#for logic Exit        
for x in blocks:
    for z in x:
        print(f'[ {z} ]', end='')
    print('')#line break