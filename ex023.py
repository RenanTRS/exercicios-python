#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#Etrada de dados----------------------------------
n = str(input('Digite um número entre 0 e 9999: ')).strip()

while n == '':
    n = str(input('Digite um número entre 0 e 9999: ')).strip()

n = int(n) #Gambiarra pois o while não estava funcionando devido ao valor vazio em uma variável int

#Manipulação de dados--------------------------------
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

#Saída de dados--------------------------------------
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#END