#Validação da primeira nota----------------------------
nota = str(input('Digite a primeira nota: ')).strip()
while nota == '' or nota.isalpha() == True:
    nota = str(input('Informe a primeira nota: ')).strip()

nota1 = float(nota)

while nota1 > 10:
    nota = str(input('Nota inválida. Informe a primeira nota: ')).strip()
    while nota == '' or nota.isalpha() == True:
        nota = str(input('Nota inválida. Informe a primeira nota: ')).strip()

    nota1 = float(nota)

#Validação da segunda nota------------------------------------------
nota = str(input('Digite a segunda nota: ')).strip()
while nota == '' or nota.isalpha() == True:
    nota = str(input('Informe a segunda nota: ')).strip()
    
nota2 = float(nota)

while nota2 > 10:
    nota = str(input('Nota inválida. Informe a segunda nota: ')).strip()
    while nota == '' or nota.isalpha() == True:
        nota = str(input('Nota inválida. Informe a segunda nota: ')).strip()

    nota2 = float(nota)

media = (nota1 + nota2)/2

#Saída------------------------
if media >= 7:
    print('APROVADO! Sua média foi: {:.1f}'.format(media))
else:
    print('REPROVADO! Sua média foi {:.1f}'.format(media))

#END