#aula 07 - Operadores Aritméticos

#Renan Souza - 08/03/2021
#Entrada de dados
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

#Manipulação de dados
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 #Serve para divisão inteira
e = n1 ** n2 #Serve para potências

#Saída dos dados
print('Soma: {}, Produto: {} e a Divisão: {:.1f}'.format(s, m, d), end=' ') #:.1f -> Serve para identificar as casas decimais
print('Divisão inteira: {} e Exponênciação: {}'.format(di, e))

#Fim