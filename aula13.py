#for c in range(0, 6): #for serve para repetir uma ação, o range é usado para indicar a quantidade de vezes
 #   print('oi')

#for c in range(6, 0, -1): #o -1 siguinifica que contará de trás para frente
#    print(c)

#for c in range (0, 7, 2): #com o dois ele pula de duas em duas vezes
#    print(c)

#n = int(input('Digite um número: '))
#for c in range(0, n+1): # o +1 serve para acrescenar mais um, dessa forma o último número é printado
#    print(c)

i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for c in range(i, f+1, p):
    print(c)

'''
n = 0
for c in range(0, 4):
    s = int(input('Digite um número: '))
    n += s
print('A soma dos valores: {}'.format(n))
'''