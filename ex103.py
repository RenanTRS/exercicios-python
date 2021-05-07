#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols 
#ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome, qtdGols):
    if nome == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {qtdGols} no campeonato.'

nome = str(input('Nome do jogador: ')).strip().title().split()[0]
qtdOfGoals = int(input('Quantidade de gols: '))

print(ficha(nome, qtdOfGoals))