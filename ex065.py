#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual
#foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

flag = 's'
maior = menor = cont = soma = 0
while flag != 'n':
    num = int(input('Digite um número: '))
    flag = str(input('Deseja continuar [S/N]:')).strip().lower()[0]
    if cont == 0:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
    soma += num
    cont += 1

print('Você digitou {} números, a média deles é {}'.format(cont, soma/cont))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
