#Crie um programa que leia uma frase qualquer e diga se é um palíndromo, desconsidenrado os espaços

frase = str(input('Digite um nome: ')).lower().split()
frase = ''.join(frase)
qtd = len(frase)-1
frase2 = ''

for c in range(qtd, -1, -1):
    frase2 += frase[c]

if frase2 == frase:
    print('{} é um palíndromo.'.format(frase2))
else:
    print('{} não é um palíndromo.'.format(frase))
    

