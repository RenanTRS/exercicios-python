#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e
#quantas já são maiores.

from datetime import date
anoAtual = date.today().year #pegando o ano da máquina do usuário
maiorIdade = menorIdade = 0

for c in range(0, 7):
    nasc = int(input('Ano em que a {}º pessoa naceu: '.format(c+1)))
    idade = anoAtual - nasc
    if idade < 18:
        menorIdade += 1
    else:
        maiorIdade += 1


print('{} São maiores de idade. '.format(maiorIdade))
print('{} São menores de idade. '.format(menorIdade))

    