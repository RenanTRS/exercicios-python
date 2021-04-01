#tuplas
'''
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim') #Tuplas ficam dentro de parênteses.

print(lanche)
print(sorted(lanche)) #Mostra em ordem
'''
#for comida in lanche:
#    print(comida)


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) #mostra quantas vezes aparece o 5
print(c.index(1)) #mostra a posição onde 1 está na tupla
del(c) #apaga a virável
print(c)
