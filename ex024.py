#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

#Entrada de dados------------------------------------------------
cidade = str(input('Em que cidade você nasceu: ')).strip().lower()

while cidade == '':
    cidade = str(input('Resposta incorreta, em que ciade você nasceu: ')).strip().lower()

#Manipulação de dados--------------------------------------------------
city = cidade.split()

#Saída de dados---------------------------------------------------------
print('{} começa com a palavra santo? {}'.format(cidade.title() , 'santo' in city[0]))
#END