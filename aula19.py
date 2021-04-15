'''
pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 24}#Declarando dicionário
#print(pessoas)
#print(pessoas['nome'])
#print(pessoas['idade'])
#print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')#aspas duplas porque as simples já estavam em uso
#print(pessoas.keys()) #mostra o nome das posições.
#print(pessoas.values()) #mostra apenas os valores.
#print(pessoas.items()) #mostra as posições e seus respectivos valores.
for k, v in pessoas.items(): #Forma de usar o for para pegar tanto às chaves como os valores
    print(k, v)
    
del pessoas['sexo'] #apaga a key e o value
print('Depois do del')
pessoas['nome'] = 'Rex' #troca de value
pessoas['peso'] = 62.0 #é possível adicionar novas keys
for k, v in pessoas.items():
    print(k, v)
'''
'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
'''
estado = dict() #Outra forma de iniciar um dicionário.
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['silga'] = str(input('Siglas do Estado: '))
    brasil.append(estado.copy()) #serve para fazer cópias, igual ao [:] das listas.
print(brasil)
