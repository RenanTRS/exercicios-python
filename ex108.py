#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números
#como um valor monetário formatado.


num = str(float(180))
#num = str(num)
num = num.replace('.', ',0')
print(f'{num}')