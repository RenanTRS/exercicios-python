#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostar que tipo de triângulo será formado: 
#Equilátero - todos os lados iguais. 
#Isósceles - dois lados iguais.
#Escaleno - todos os lados diferentes.

r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    #print('triângulo')
    if r1 == r2 == r3:
        print('Triângulo Equilátero.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('Estas retas não formam um triângulo.')

#END