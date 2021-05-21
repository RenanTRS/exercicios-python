def aumentar(num, taxaB):
    porc = (num * taxaB) / 100
    return formatar(num + porc)

def diminuir(num, taxaS):
    porc = (num * taxaS) / 100
    return formatar(num - porc)

def metade(num):
    valor = num / 2
    return formatar(valor)

def dobro(num):
    valor = num * 2
    return formatar(valor)

def formatar(num):
    return f'{num:.2f}'.replace('.', ',')


def resumo(num, taxaB=0, taxaS=0):
    print(f'Preço analizado R${formatar(num):>5}')
    print(f'A metade de R${formatar(num)} é R${metade(num)}')
    print(f'O dobro de R${formatar(num)} é R${dobro(num)}')
    print(f'Com mais {taxaB}% de R${formatar(num)} é R${aumentar(num, taxaB)}')
    print(f'Com menos {taxaS}% de R${formatar(num)} é R${diminuir(num, taxaS)}')
