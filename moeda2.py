def aumentar(num):
    valor = (num * 10) / 100
    novoValor = formatar(valor+num)
    print(f'Aumentando 10% temos R${novoValor}')

def diminuir(num):
    return num

def dobro(num):
    novoNum = num * 2
    numf = formatar(num)
    novoNum = formatar(novoNum)
    print(f'O dobro de R${numf} é R${novoNum}')

def metade(num):
    numf = formatar(num)
    novoNum = num / 2
    novoNum = formatar(novoNum)
    print(f'A metade de R${numf} é R${novoNum}')

def formatar(num):
    numf = str(num)
    numf = numf.replace('.', ',0')
    return numf