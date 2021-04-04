'''
num = [5, 8, 7, 2] #lista
print(num)
num[2] = 9 #É possível trocar o item da lista desta forma
print(num)
num.insert(2, 0)#inserir o zero na posição 2
print(num)
num.append(1)#Desta forma se adicionar um item a lista
print(num)
num.sort()#O metodo sort coloca a função em ordem crescente
print(num)
print(num.sort(reverse=True)) #Coloca em ordem decrescente
print(len(num)) #função len() mostra quantos elementos a lista possui
num.pop()#pop para remover, sem parametro remove o último
print(num)
num.pop(2)#pop para remover, com parametro remove a posição indicada
print(num)
num.remove(8)#Remove o valor indicado, neste caso foi o 8
print(num)
'''
'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for e, c in enumerate(valores):
    print(f'Na posição {e} encontrei o valor: {c}')
'''
'''
valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: '))) #usar o for para colocar valores

print(valores)
'''

a = [5, 8, 7, 9, 0]
#b = a#Além de receber o valor também é feita uma ligação, se algo for alterado em b também será alterado em a
b = a[:]#Forma correta de transferir um valor para o outro sem criar uma ligação
b[3] = 1
print(a)
print(b)