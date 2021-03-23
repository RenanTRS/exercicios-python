#Refaça o desafio 009, mostrando a tabuada de um número que o usuáiro escolher, só que agora utilizando um laço for.

n = int(input('Digite um número: '))
for c in range(1, 11):
    print('{}x{}={}'.format(n, c, n * c))