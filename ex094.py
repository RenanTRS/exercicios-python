#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os 
#dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

#functions
def average(a, b):
    averageAge = a / b
    return averageAge

def lineBreak():
    print()

#variables
person = {}
people = []
age = 0

#while logic
while True:
    #inputs
    person['name'] = str(input('Name: ')).strip().title().split()[0]
    person['sex'] = str(input('Sex [M/F]: ')).strip().upper().split()[0]
    #if error logic
    if person['sex'] != 'M' and person['sex'] != 'F':
        #while logic
        while True:
            person['sex'] = str(input('Error, just input M or F: ')).strip().upper().split()[0]
            if person['sex'] == 'M' or person['sex'] == 'F':
                break

    person['age'] = int(input('Age: '))
    
    age += person['age']
    people.append(person.copy()) #copy to list
    
    #flag
    opt = str(input('Do you want to continue [Y/N]:')).strip().upper().split()[0]
    if 'N' in opt:
        break

#exit    
print(people)
averageAge = average(age, len(people))
print(f'{averageAge:.1f}')
print(f'Registered women:', end=' ')
for c in people:
    if c['sex'] == 'F':
        print(c['name'], end=' ')
lineBreak()

print('Above average people:', end=' ')
for c in people:
    if c['age'] > averageAge:
        print(c['name'], end=' ')
lineBreak()