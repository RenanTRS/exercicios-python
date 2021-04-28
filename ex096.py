#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e 
#mostre a área do terreno.

def area(w, l):
    landControl = w * l
    print(f'The area of a {w} x {l} plot is {landControl}m²')

print('Land Control')
w = float(input('Width: '))
l = float(input('Length: '))

area(w, l)