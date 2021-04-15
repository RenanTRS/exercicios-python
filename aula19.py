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
