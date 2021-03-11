#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Informe a quantidade de metros: '))

cm = m * 100
mm = m * 1000

print('Cm: {} \nMm: {}'.format(cm, mm))