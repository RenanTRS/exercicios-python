'''
def lin(): #Declarando função
    print('-'*30)

lin() #Chamando função
print('   Curso em vídeo   ')
lin()
'''
'''
def lin():
    print('-'*30)
def mensagem(msg):
    lin() #chamando uma função dentro de outra função
    print(msg)
    lin()

mensagem('  CURSO EM VÍDEO   ')
'''
'''
def soma(a, b):
    s = a + b
    print(s)

soma(3, 2)
soma(4, 5)
soma(2, 2)
'''
'''
def contador(*num): #*num é um desempacotador, serve para receber uma quantidade incerta de valores.
    tam = len(num)
    print(f'Recebi os valores {num} e são {tam} números.')
    for i in num:
        print(i, end=' ')
    print('fim')

contador(3, 5, 6)
contador(1, 2)
contador(6, 5, 4)
'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [4, 5, 2, 1]
dobra(valores)
print(valores)