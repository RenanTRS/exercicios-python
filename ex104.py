#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo 
#a validação para aceitar apenas um valor numérico.

def leiaInt(num='vazio'):
    if num.isnumeric() == False:
        while True:
            print('\033[1;31mErro, Digite um número inteiro.\033[m')
            num = str(input('Digite um número: '))
            #flag
            if num.isnumeric():
                break
    return num

num = leiaInt(input('Digite um número: '))
print(f'Você digitou o número {num}')
