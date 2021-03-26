#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura
#while.

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
cont = 9

print('{} -> '.format(primeiroTermo), end='')
while cont >= 1:
    primeiroTermo += razao
    if cont == 1:
        print('{}'.format(primeiroTermo))
        cont -= 1
    else:
        print('{} -> '.format(primeiroTermo), end='')
        cont -= 1
