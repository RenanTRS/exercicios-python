'''
def somar(a=0, b=0, c=0): #atribuindo o valor 0 ele passa a ser o valor padrão, para caso o valor não seja passado pelo parâmetro.
    s = a + b + c
    print(s)


somar(4, 2, 1)
somar(4, 2)
somar(4)
somar()
'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s #retorna um resultado

s1 = somar(4, 2, 1) #variável s1 recebe o retorno da função
s2 = somar(4, 2)
s3 = somar(4)

print(f'Resultado das somas: {s1}, {s2}, {s3}')