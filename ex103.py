#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols 
#ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome, qtdGols=0):
    if nome == '':
        nome = '<desconhecido>'
    if qtdGols.isnumeric() == False:
        qtdGols = 0
    return f'O jogador {nome} fez {qtdGols} no campeonato.'

nome = str(input('Nome do jogador: ')).strip().title()
qtdOfGoals = str(input('Quantidade de gols: '))

print(ficha(nome, qtdOfGoals))