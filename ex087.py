#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

#variables
blocks = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pair = sColumn = bigger = 0

#for logic
for l in range(0, 3):
    for c in range(0, 3):
        blocks[l][c] =  int(input(f'Enter a number for [{l}, {c}]: '))

        if blocks[l][c] % 2 == 0:
            pair += blocks[l][c]
        
        if c == 2:
            sColumn += blocks[l][c] #sum of third column
        
        if l == 1:
            if c == 0:
                bigger = blocks[l][c]
        
            else:
                if bigger < blocks[l][c]:
                    bigger = blocks[l][c]

#code exit
print('='*22)
for s in blocks:
    for b in s:
        print(f'[{b:^5}]', end='')
    print()#line break

print(f'Sum of even values: {pair}')
print(f'Sum of third column: {sColumn}')
print(f'The bigger of the second row: {bigger}')
