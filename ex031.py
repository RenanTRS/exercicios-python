#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
#km para viagens até 200km e 0,45 para viagens mais longas

dist = float(input('Informe a distância da viagem: '))

if dist > 200:
    valor = dist * 0.45
else:
    valor = dist * 0.50
    
print('Para uma viagem de {}Km, custará R${:.2f}'.format(dist, valor))
