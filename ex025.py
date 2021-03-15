#Crie um programe que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

#Entrada de dados-----------------------------------
nome = str(input('Digite o seu nome completo: ')).strip().lower()

while nome == '':
    nome = str(input('Valor inválido. Digigte o seu nome completo: ')).strip().lower()

#Saída de dados--------------------------------------------------
print('Nome: {}'.format(nome.title()))
print('Contém o nome Silva: {}'.format('silva' in nome))
#END