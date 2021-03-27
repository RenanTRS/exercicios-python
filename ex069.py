#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 

opc = sexo = ' '
maiorIdade = homem = mulher20 = 0
while True:
    nome = str(input('Digite o nome: ')).strip().title()
    
    #Sexo-----------------------------------------------------
    sexo = str(input('Informe o sexo: ')).strip().lower()[0]
    while sexo not in 'mf':
        sexo = str(input('Informe o sexo: ')).strip().lower()[0]
    
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        maiorIdade += 1
    
    if sexo == 'm':
        homem += 1
    elif sexo == 'f' and idade < 20:
        mulher20 += 1
    
    #Flag------------------------------------------------------------
    opc = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if opc == 'n':
        break

print(f'Total de pessoas maiores de idade: {maiorIdade}')
print(f'Homens cadastrados: {homem}')
print(f'Mulheres com menos de 20 anos: {mulher20}')
