'''# teste de igualdade
melhor_linguagem = "Python".lower()
int_num = 1001
float_num = 10.01
resp = melhor_linguagem == "python"
print(resp)

# testando uma desigualdade

resp1 = melhor_linguagem != "Python"
print(resp1)


# Comparações Númericas
idade = 21
print(idade > 18)
print(idade > 22)
print(idade >= 21)
print(idade < 50)
print(idade < 21)
print(idade <= 21)
# Operadores de Comparação


# Combiando testes condicionais
# and - só retorna True quando todas condições retornarem True
# or - Ele retorna True quando pelo meos uma condição retorna True
idade1 = 21
idade2 = 17

print(idade1 > 18 and idade2 > 18)
# False
print(idade1 <= 25 and idade2 <= 25)
# True
print(idade1 > 18 or idade2 > 18)
# True
print(idade1 <= 15 or idade2 <= 15)
# False


# Testando se um valor é elemento de uma lista
# x in my_list: Retorna True se na lista my_list algum elemento igual a x

usuarios = ['potinho', 'potinho123', 'potinho_gamer']
print('potinho' in usuarios)
print('dudu' not in usuarios)
print('potinho' not in usuarios)


usuario_ativo = True
print(type(usuario_ativo))


# Comando if
# if teste_condicional1:
#   faça alguma coisa   # se teste_condicional1 == True
# elif teste_condicional2
#   faça alguma coisa # executando se teste_condicional2 == True
# else:
#   aça alguma outra coisa # executando se teste_condicional == False

idade = 17
if idade >= 18:
    print("Você já tem idade para dirigir!")
    print("Já fez a matrícula na auto escola?")
else:
    print("Você não tem idade para dirigir!")


rodizio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
resp = int(input("Qual o final da sua placa? "))
if resp == 1 or resp == 2:
    print("Hoje é segunda você, não pode sair")
elif resp == 3 or resp == 4:
    print("Hoje é terça, você não pode sair")
elif resp == 5 or resp == 6:
    print("Hoje é quarta, você não pode sair")
elif resp == 7 or resp == 8:
    print("Hoje é quinta, você não pode sair")
elif resp == 9 or resp == 0:
    print("Hoje é sexta, você não pode sair")
------------------------------------------------------
pedidos = ['frango', 'carne', 'kafta', 'medalhão']

for pedido in pedidos:
    if pedido == "frango":
        print("Desculpe estamos sem frango no momento")
    else:
        print(f"Estão sendo preparados {pedido}")
------------------------------------------------------
lista_vazia = []

if lista_vazia:
    print("Teste 1")
else:
    print("Teste 2")
'''
pedidos = ['frango', 'carne', 'kafta', 'medalhão']
pedidos_disponiveis = ['frango', 'pizza', 'batata frita', 'esfiha']

for pedido in pedidos_disponiveis:
    if pedido == "frango":
        print(f"Preparando {pedido}")
    else:
        print(f"Desculpe estamos sem {pedido} no momento")
