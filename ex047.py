#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(0, 51):
    if c % 2 == 0:
        print(c, end=' ')

print() #apenas para o compilador pular uma linha no terminal.
