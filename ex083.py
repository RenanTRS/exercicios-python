#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão 
#passada está com os parênteses abertos e fechados na ordem correta.

expression = input('Enter a expression: ')

ope = expression.count('(')
closed = expression.count(')')
if ope == closed:
    print('Valid expression')
else:
    print('Invalid expression')