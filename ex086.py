#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na 
#tela, com a formatação correta.

blocks = [[0, 0, 0], [0, 0, 0], [0, 0, 0,]]

for c in range(0, 3):
    for y in range(0, 3):
        blocks[c][y] = int(input(f'Enter a number for [{c}, {y}]: '))
        
for x in blocks:
    print(x)