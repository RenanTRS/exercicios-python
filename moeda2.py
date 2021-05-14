def aumentar(num):
    valor = (num * 10) / 100
    return valor + num

def dobro(num):
    return num * 2

def metade(num):
    return num / 2

def formatar(preco):
    return f'{preco:.2f}'.replace('.', ',')