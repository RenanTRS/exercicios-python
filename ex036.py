#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
#do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo
#será negado

casav = float(input('Digite o valor da casa R$'))
sal = float(input('Digite o seu salário R$'))
anos = int(input('Digite em quantos anos você pretente pagar o empréstimo: '))

parcela = casav / (anos * 12)
limite = (sal * 30)/100

print('--'*20)
if parcela <= limite:
    print('\033[1mValor do Empréstimo: R${:.2f}'.format(casav))
    print('\033[1mValor da Prestação: R${:.2f}'.format(parcela))
    print('\033[1mValor limite de parcela: \033[1;32mR${:.2f}\033[m'.format(limite))
    print('\033[1;32mEmpréstimo Aprovado!\033[m')

else:
    print('\033[1mValor do Empréstimo: R${:.2f}'.format(casav))
    print('\033[1mValor da Prestação: R${:.2f}'.format(parcela))
    print('\033[1mValor limite de parcela: \033[1;31mR${:.2f}\033[m'.format(limite))
    print('\033[1;31mEmpréstimo Negado!\033[m')