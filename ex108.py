#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números
#como um valor monetário formatado.

import moeda2

num = float(input('Digite o preço R$'))
print(f'A metade de R${moeda2.formatar(num)} é R${moeda2.formatar(moeda2.metade(num))}')
print(f'O dobro de R${moeda2.formatar(num)} é R${moeda2.formatar(moeda2.dobro(num))}')
print(f'10% de R${moeda2.formatar(num)} é R${moeda2.formatar(moeda2.aumentar(num))}')

