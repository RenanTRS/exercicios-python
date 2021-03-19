#Escreva um programa que leia um número inteiro qualquer e peça para o usário escolher qual será a base de 
#conversão: 1 -binário, 2 - octal, 3 - hexadecimal

num = int(input('Digite um número: '))
escolha = int(input('Escolha:\n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\n'))

if escolha == 1:
    print('O número {} em binário: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} em octal: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} em hexadecimal: {}'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mOpção inválida!\033[m')