#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando 
#um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(year):
    from datetime import date
    toDay = date.today().year
    age = toDay - year

    if age < 16:
        sit = 'Denied'
    elif age < 18 or age > 65:
        sit = 'Optional'
    else:
        sit = 'Mandatory'
        
    return f'At {age} years old, voting is {sit}'

year = int(input('What year were your born? '))
print(voto(year))