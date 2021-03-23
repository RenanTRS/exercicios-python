#Faça um programa que calcule a soma e entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 
#1 até 500

cont = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s += c

print('A soma dos ímpares e múltiplos de 3: {}'.format(s))
