#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um 
#programa que importe esse módulo e use algumas dessas funções.

import moeda

num = float(input('Digite o preço R$'))
moeda.metade(num)
moeda.dobro(num)
moeda.aumentar(num)