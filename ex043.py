#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de 
#acordo com a tabela abaixo: 
#Abaixo de 18.5 - Abaixo do peso. 
#Entre 18.5 e 25 - Peso ideal.

#IMC = peso (em quilos) ÷ altura² (em metros)
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('\033[1;31m{:.1f}\033[m Você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('\033[1;32m{:.1f}\033[m Você está no peso ideal.'.format(imc))
else:
    print('\033[1;31m{:.1f}\033[m Você está acima do peso.'.format(imc))

#END