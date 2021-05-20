#Modifique as funções que forma criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado 
#por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda3
num = float(input('Digite um preço R$'))
print(f'A metade de R${moeda3.formatar(num)} é {moeda3.metade(num)}')
print(f'O dobro de R${moeda3.formatar(num)} é {moeda3.dobro(num)}')
print(f'10% de R${moeda3.formatar(num)} é {moeda3.aumentar(num)}')