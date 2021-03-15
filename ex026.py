#Faça um programa que leia uma frase pelo teclado e mostre: Qantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

#Entrada de dados-----------------------------------------
frase = str(input('Digite uma frase: ')).strip().lower()

while frase == '':
    frase = str(input('Digite uma frase: ')).strip().lower()

#Manipulação de dados---------------------------------------
qtd = frase.count('a') #Contar a quantidade de "a" na variável "frase"
l = frase.find('a') + 1
r = frase.rfind('a') + 1

#Saída de dados---------------------------------------------
print('Quantas vezes apareceram a letra "A": {}'.format(qtd))
print('Em que posição a letra "A" aparece pela primeira vez: {}'.format(l))
print('Em que posição a letra "A" aparece pela última vez: {}'.format(r))

#END