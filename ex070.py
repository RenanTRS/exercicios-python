# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No 
#final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 

soma = maisMil = cont = 0
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    valor = float(input('Valor do produto: '))
    cont += 1
    soma += valor
    if valor > 1000:
        maisMil += 1
    if cont == 1:
        barato = produto
        maisBarato = valor
    else:
        if maisBarato > valor:
            maisBarato = valor
            barato = produto
    
    flag = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if flag == 'n':
        break
print('=='*20)
print(f'Total gasto R${soma:.2f}')
print(f'{maisMil} custam mais que R$1000,00')
print(f'{barato} é o produto mais barato.')