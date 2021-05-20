def aumentar(num):
    valor = (num * 10) / 100
    return formatar(valor+num)

def dobro(num):
    valor = num * 2
    return formatar(valor)

def metade(num):
    valor = num / 2
    return formatar(valor)

def formatar(preco):
    return f'{preco:.2f}'.replace('.', ',')