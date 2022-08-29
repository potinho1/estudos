# Exceções

# Programa vulnerável contra erros de divisão por zero e de conversão

print("Forneça dois números e eu retorno o valor da divião entre eles.")
print("Entre com 's' para sair a qualquer momento para finalizar.")

"""
while True:
    num_1 = input("Primeiro número: ")
    if num_1 == 's':
        break
    num_2 = input("Segundo número: ")
    if num_1 == 's':
        break
    resultado = float(num_1) / float(num_2)
    print(f"{num_1} / {num_2} = {resultado}")


Blocos try, except e else
    try: 
        Aqui vai o código que pode gerar algum erro
    except:
        Aqui nós especificamos o que deve acontecer quando um erro for gerado
    else:
        Aqui nós especificamos o que acontece se nenhuma excerção é gerada


# Programa protegido contra erros de divisão por zero e erros de conversão
while True:
    num_1 = input("Primeiro número: ")
    if num_1 == 's':
        break
    num_2 = input("Segundo número: ")
    if num_1 == 's':
        break
    try:
        resultado = float(num_1) / float(num_2)
    except:
        print("Algum erro foi gerado. Tente novamente.")
    else:
        print(f"{num_1} / {num_2} = {resultado}")

"""

# Programa protegido contra erros de divisão por zero, especificando a exceção

while True:
    num_1 = input("Primeiro número: ")
    if num_1 == 's':
        break
    num_2 = input("Segundo número: ")
    if num_1 == 's':
        break
    try:
        resultado = float(num_1) / float(num_2)
    except ZeroDivisionError:
        print("É impossível dividir por zero.")
    except ValueError:
        print("O valor fornecido é inválido")
    except:
        print("Algum erro inesperado foi gerado. Por favor tente novamente.")
    else:
        print(f"{num_1} / {num_2} = {resultado}")
