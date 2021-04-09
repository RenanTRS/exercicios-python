'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 60
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Joaquim', 13], ['Maria', 22], ['Fulano', 22]]
print(galera)
print(galera[2]) #mostra todo o conteúdo do índicie
print(galera[2][0])#mostra apenas um conteúdo específico do indicie dentro de um índicie

print('------------')
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
    #print(p[0])
'''
galera = []
dados = []
totmaior = totmenor = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])#O [:] serve para passar uma cópia de todo o conteúdo da lista sem conexão alguma
    dados.clear() #O .clear() serve para limpar a lista

for p in galera:
    if p[1] < 18:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
    else:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1

print(f'A lista possui {totmaior} maiores de idade e {totmenor} menores de idade.')

