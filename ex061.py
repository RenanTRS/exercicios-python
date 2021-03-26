#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura
#while.

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
cont = 1

while cont <= 10:
    if cont < 10:
        print('{} -> '.format(primeiroTermo), end='')
    else:
        print('{} '.format(primeiroTermo))
    
    primeiroTermo += razao
    cont += 1
