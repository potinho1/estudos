'''lista_conta = ['agua', 'luz', 'net', 'carro', 'amazon']

for conta in lista_conta:
    print(f"Não posso esquecer de pagar {conta}")
print("Essas são minhas contas a pagar")

lista = ['luz', 'agua', 'energia', 'net', 'carro']
------------------------------------------------------->
for conta in lista:
    print("Lembrete:")
    print(f"Não esqueci de pagar {conta}")
print("Essas as contas que preciso pagar esse mês")


# Sequencia de 1 a 100
for num in range(1, 101, 1):
    print(num)


# range sem o for
num = list(range(1, 101, 1))
print(num)

# Criar um sequencia apenas por números ímpares, de 1 até 15
# Com for
for num in range(1, 16, 2):
    print(num)

# Com listas
num = list(range(1, 16, 2))
print(num)

# Criar uma sequencia com os primeros 10 quadrados(1, 4, 9....)
quadrados = []
for num in range(1, 11):
    quadrados.append(num**2)
print(quadrados)

# Soma da lista
print(sum(quadrados))

# Maior valor na lista
print(max(quadrados))

# Menor valor na lista
print(min(quadrados))

# Mostrar as três ultimas pontuações
game_scores = [50, 56, 64, 33, 47, 89, 32, 57, 24, 99, 21]

# slice é um grupo de itens de uma lista
print(game_scores[0:4])  # O número da direta não é exibido

# Pegar os três primeiros
print(game_scores[0:3])

# Pegar os três ultimos
print(game_scores[-3:])

# Meio da lista
print(game_scores[2:5])

# Se não especificar o primeiro indice ele vai pegar do 0: ate o numero desejado
print(game_scores[:5])

# Sem especificar o ultimo, ele pula o numero idicado na esquerda e vai ate o final da lista
print(game_scores[2:])

# pular casas
print(game_scores[0:9:2])


# Ordenar lsitas
game_scores = [50, 56, 64, 33, 47, 89, 32, 57, 24, 99, 21]
sorted_scores = sorted(game_scores, reverse=True)
print(sorted_scores)

print("5 maiores pontuações:")
i = 1
for score in sorted_scores[:5]:
    print(f"{i}: {score}")
    i = i + 1

# Acrescentar estados na lista
sudeste = ['SP', 'RJ', 'MG', 'ES']
estados = sudeste
estados.append("BA")
estados.append("GO")
estados.append("SC")
print(estados)

# redefinir a lista
sudeste = ['SP', 'RJ', 'MG', 'ES']
estados = sudeste[:]
estados.append("BA")
estados.append("GO")
estados.append("SC")
print(estados)
print(sudeste)


# Listas são mutáveis, listas podem serem alteradas

# TUPLES
# Ultilizar () para tuples
# Não pode alterar elementos de tuples
my_tuple = (50, 300)
print(my_tuple[1])

# Criar um novo tuple com o mesmo nome pode
my_tuple = (50, 300, 100)
print(my_tuple)
'''

my_tuple = (50, 300)

for valor in my_tuple:
    print(valor)
