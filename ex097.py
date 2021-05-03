#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com 
#tamanho adaptável.

def showMe(txt):
    width = len(txt)+4
    print('~'*width)
    print(f'{txt.center(width)}') #.center() biblioteca padrão pra alinhar strings
    print('~'*width)

showMe('Renan')
showMe('Curso de Python no YouTube')
showMe('CeV')