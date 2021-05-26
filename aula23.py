#Tratamento de erros

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError): #Mais de um tipo de erro em dentro do mesme except
    print("Tivemos um problema com os tipos de dados que você digitou")
except ZeroDivisionError: #Divisão por zero
    print("Não é possível dividir um número por 0")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados.") #Quando o usuário interrompe o programa
except Exception as erro: #usando a classe Exception e criando objeto com a referência erro, igual a catch(Exception ex){} no java
    print(f"erro encontrado {erro.__class__}") #mostra a class do erro
else:
    print(f'{r}')

'''
except: #seria o cath do java ou algo parecido
    print("Ops! Houve um erro.")

#OPCIONAIS
else:
    print(f"Resultado {r}")

finally: #Sempre ocorre dando erro ou não
    print('Obrigado volte sempre!')
'''
