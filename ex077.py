#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, 
#quais são as suas vogais.

palavras = ('teste', 'python', 'rex', 'mayuko')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in palavras:
    print(f'{c.upper()} ', end = ' ')
    for y in c:
        if y in vogais:
            print(y, end=' ')
    print('')