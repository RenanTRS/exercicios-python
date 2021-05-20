def aumentar(num, taxa):
    valor = (num * taxa) / 100
    return formatar(valor)

def formatar(num):
    return f'R${num:.2f}'.replace('.', ',')

def resumo(num, taxaB, taxaS):
    print(f'Preço analizado {formatar(num):>5}')
