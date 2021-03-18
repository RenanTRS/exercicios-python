#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a basae de conversão:
#1 para binário, 2 para octal, e 3 para hexadecimal

import binascii
import binhex
num = int(input('Digite um número: '))
escolha = int(input('[1] - Binário \n[2] - Octal \n[3] - Hexadecimal\n'))

if escolha == 1:
    n = bin(num)
    print(bin(num)[2:])
elif escolha == 2:
    print(oct(num)[2:])
elif escolha == 3:
    print(hex(num)[2:])
