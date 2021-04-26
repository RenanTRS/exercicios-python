#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os 
#dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

person = {}
people = []

#while logic
while True:
    person['name'] = str(input('Name: ')).strip().title().split()[0]
    person['sex'] = str(input('Sex [M/F]: ')).strip().upper().split()[0]
    
    #if logic
    if person['sex'] != 'M' and person['sex'] != 'F':
        #while logic
        while True:
            person['sex'] = str(input('Error, just input M or F: ')).strip().upper().split()[0]
            if person['sex'] == 'M' or person['sex'] == 'F':
                break

    person['age'] = int(input('Age: '))
    people.append(person.copy())
    
    #flag
    opt = str(input('Do you want to continue [Y/N]:')).strip().upper().split()[0]
    if 'N' in opt:
        break

print(people)
