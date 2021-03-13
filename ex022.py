#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao no total (sem considerar espaços). Quantas letras tem o primeiro nome

#Entrada de dados--------------------------------
nome = str(input('Digite o seu nome: '))

#Manipulação de dados-----------------------------
nome = nome.strip() #Remover espaços
sepa = nome.split() #Dividindo em lista
qtd = len(''.join(sepa)) #Juntando os caracteres
n1 = len(sepa[0]) #Contando o item 0 da lista

#Saída de dados-----------------------------------
print('Seu nome completo com letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome completo com letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras do seu nome: {}'.format(qtd))
print('O nome {} tem {} letras'.format(sepa[0].capitalize(), n1))

#END