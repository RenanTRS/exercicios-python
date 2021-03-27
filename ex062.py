#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser 
#que quer mostrar 0 termos.

primeiroT = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
final = 10
opc = True
termos = 10

while opc == True:
    while cont <= final:
        print('{} -> '.format(primeiroT), end='')
        primeiroT += razao
        cont += 1
    print('PAUSA')
    qtd = int(input('Quantos termos você deseja ver: '))
    if qtd > 0:
        final = qtd
        cont = 1
        termos += qtd
    else:
        opc = False

print('Progressão finalizada com {} termos mostrados.'.format(termos))
