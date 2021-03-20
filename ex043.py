#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de 
#acordo com a tabela abaixo: 
#Abaixo de 18.5 - Abaixo do peso. 
#Entre 18.5 e 25 - Peso ideal.
#25 até 30 - Sobrepeso
#30 até 40 - Obesidade
#Acima de 40 - Obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('{:.1f} Você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('\033[1;32m{:.1f}\033[m Você está no peso ideal.'.format(imc))
elif imc < 30:
    print('{:.1f} Você está Sobrepeso'.format(imc))
elif imc < 40:
    print('{:.1f} Você está com Obesidade'.format(imc))
else:
    print('{:.1f} Obesidade mórbida.'.format(imc))

#END