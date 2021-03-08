#!---#ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele

#Renan Souza - 08/03/2021

#Etrada de dados
msg = input("Digite uma mensagem: ")

#Saída de dados
print("O tipo primitivo é:{}".format(type(msg)))
print("Somente numeros? ", msg.isnumeric()) #Verifica se são apenas números
print("Somente espaços? ", msg.isspace()) #Verifica se possui apenas espaços em branco
print("Somente letras? ", msg.isalpha()) #Verifica se possui letras
print("Possui letras e números? ", msg.isalnum()) #Verifica se possui letras e números
print("Maíusculas? ", msg.isupper()) #Verifica se tudo está em maiúsculo
print("Minúsculas? ", msg.islower()) #Verifica se tudo está em minúsculo
print("Está capitalizado? ", msg.istitle()) #Verifica se a str está capitalizada

#Fim