# Aula 8: Criando funções para automatizar o seu código.

# O que é função?
# É um bloco de código criado para resolver um problema especifico. Este bloco de código recebe um nome, e toda vez que precisamos realizar a tarefa definida pela função, basta chamar essa função.

# Funções tomam o seu código mais fácil de:
# . Ler e entender
# . Testar
# . Modificar
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->

# Boas vindas
'''
def boas_vindas():
    #Mostra uma mensagem de boas vindas
    print("Seja muito bem vindo!")


boas_vindas()


# Mostrando uma mensagem personalizada
def boas_vindas(nome):
    # Mostra uma mensagem de boas vindas
    print(f"Seja muito bem vindo!, {nome}")


boas_vindas("Potinho")

# Parâmetro VS Argumento

# Passando argumentos para uma função

#Positional Arguments
def info_funcionario(nome, cargo, salario):
    print(f"Nome do funcionário: {nome}")
    print(f"Cargo do funcionário: {cargo}")
    print(f"Salário do funcionário: {salario}")


info_funcionario("potinho", "dev", 5000)


# Keyword arguments

def info_funcionario(nome, cargo, salario):
    print(f"Nome do funcionário: {nome}")
    print(f"Cargo do funcionário: {cargo}")
    print(f"Salário do funcionário: {salario}")


info_funcionario(nome="potinho", cargo="dev", salario=5000)
info_funcionario(salario=5000, cargo="dev", nome="potinho")


# Valores padrão


def info_funcionario(nome, salario, cargo="dev"):
    print(f"Nome do funcionário: {nome}")
    print(f"Cargo do funcionário: {cargo}")
    print(f"Salário do funcionário: {salario}")


info_funcionario(nome="potinho", salario=3000)
info_funcionario(nome="potinho", salario=3000, cargo="infra")


# Sem especificar o argumento para "cargo", positional arguments


def info_funcionario(nome, salario, cargo="dev"):
    print(f"Nome do funcionário: {nome}")
    print(f"Cargo do funcionário: {cargo}")
    print(f"Salário do funcionário: {salario}")


info_funcionario(nome="potinho", salario=3000)
print("\n")
info_funcionario("potinho", 5000, "dev")
print("\n")
info_funcionario("potinho", 5000)
print("\n")
info_funcionario(nome="potinho", salario=5000, cargo="dev")
'''
# Funções que retorna valores


def quadrado(num):
    return num ** 2


print(quadrado(2))

my_square = quadrado(5)
print(my_square)

numero = 7
print(f"O quadrado de {numero} é igual a {quadrado(numero)}")


# Funções podem retornar listas, dicionarios, tupulas.

# Retornando um dicionário
