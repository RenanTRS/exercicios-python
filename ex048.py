#Faça um programa que calcule a soma e entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 
#1 até 500

cont = 0
s = 0
for c in range(1, 501):
    num = cont * 3
    cont += 1
    if num % 2 != 0 and num <= 50:
        print(num)
        s += num

print('Soma dos ímpares e múltiplos de 3: {}'.format(s))