#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes
#informações:
#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)

def notas(*n, sit=False):
    cont = media = 0
    for c in n:
        if cont == 0:
            maior = c
            menor = c
            cont += 1
        
        if c > maior:
            maior = c
        
        if c < menor:
            menor = c
        
        media += c
    media /= 4
    aluno = {'maior': maior, 'menor': menor, 'media': media}
    if sit:
        if media <= 5:
            aluno['situacao'] = 'Ruim'
        elif media > 5:
            aluno['situacao'] = 'Boa'

    return aluno


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)