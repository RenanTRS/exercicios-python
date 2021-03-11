#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input('Informe em metros a largura da parede: '))
a = float(input('Informe em metros a altura da parede: '))

area = l * a
tinta = area / 2

print('A parede possui {}m²'.format(area))
print('Precisa-se de {}l de tinta'.format(tinta))

