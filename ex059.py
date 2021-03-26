#Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números
#[ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
flag = True

while flag == True:    
    print('=-='*20)
    escolha = int(input('[1] - Somar \n[2] - Multiplicar \n[3] - Maior \n[4] - Novos números \n[5] - Sair do programa\n'))

    if escolha == 1:#1----------------------------------------------------------
        print('Soma: {}'.format(num1 + num2))

    elif escolha == 2:#2---------------------------------------------------------
        print('Multiplicação: {}'.format(num1 * num2))

    elif escolha == 3: #3---------------------------------------------------------
        if num1 > num2:
            print('{} é o número maior.'.format(num1))
        elif num1 < num2:
            print('{} é o número maior.'.format(num2))
        else:
            print('Não existe número maior, os valores são iguais.')

    elif escolha == 4: #4---------------------------------------------------------
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite um novo número: '))

    elif escolha ==5:#5------------------------------------------------------------
        flag = False
        print('Saíndo....')
        sleep(1)
    
    else:
        print('Escolha inválida.')
#Fim do laco-----------------------------------------------------------------------------------
print('Fim')
