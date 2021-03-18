#Condições aninhadas

nome = str(input('Digite seu nome: ')).strip().title()
if nome == 'Renan':
    print('Que nome bonito!')
elif nome == 'Kimeuton':
    print('Cê veio de Marte?')
elif nome in 'Ana Claudia Brenda':
    print('Belo nome feminino.')
elif nome == 'Maria' or nome == 'João' or nome == 'José':
    print('Seu nome é bem popular no brasil.')
else:
    print('Seu nome é tão normal.')

print('Tenha um bom dia \033[1;33m{}\033[m'.format(nome))