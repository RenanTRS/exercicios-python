#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que 
#analisar todos os valores e dizer qual deles é o maior.

#functions
def breakLine():
    print('-='*20)
def maior(*num):
    count = bigger = 0
    for c in num:
        print(c, end=' ')
        if count == 0:
            bigger = c
            count += 1
        elif bigger < c:
            bigger = c
    print(f'Foram informados {len(num)} ao todo.')
    print('O maior valor informado foi: ',bigger)
    breakLine()


    #breakLine()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()