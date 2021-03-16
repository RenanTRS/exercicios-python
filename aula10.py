n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2)/2

if media >= 7:
    print('APROVADO! Sua média foi: {:.1f}'.format(media))
else:
    print('REPROVADO! Sua média foi {:.1f}'.format(media))
