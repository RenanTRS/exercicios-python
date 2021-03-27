#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que 
#é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


soma = num = cont = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        flag = 999
    else:
        soma += num
        cont += 1

print('Você digitou {} números, e a soma entre eles foi {}'.format(cont, soma))
