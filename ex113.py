#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mErro, por favor digite novamente\033[m")
        except KeyboardInterrupt:
            print("\033[1;31mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mErro, por favor digite novamente\033[m")
        except (KeyboardInterrupt):
            print("\033[1;31mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return n

numInt = leiaInt("Digite um número inteiro: ")
print(f"O valor digitado foi {numInt}")

numFloat = leiaFloat("Digite um número float: ")
print(f"O valor digitado foi {numFloat}")