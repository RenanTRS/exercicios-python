#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
c = float(input('Informe a temperatura em C: '))

f = ((9 * c) / 5)+32

print('A temperatura {}Cº é equivalente à {}Fº'.format(c, f))
