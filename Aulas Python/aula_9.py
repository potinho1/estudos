# Criando funções para automatizar o seu código.

# Criar a função para mmostrar as pontuações de maneira organizada.
'''
def mostrar_pontuacoes(lista_pontuacoes):
    """ Mostrar as pontuações dos jogadores de maniera organizada """
    for pontuacao in lista_pontuacoes:
        print(
            f"{pontuacao['nome_jogador']} fez {pontuacao['pontuação']} pontos \n")


pontuacoes_jogadores = [
    {'nome_jogador': "Potinho", 'pontuação': 100},
    {'nome_jogador': "ana", 'pontuação': 80},
    {'nome_jogador': "laura", 'pontuação': 50},
]


mostrar_pontuacoes(pontuacoes_jogadores)
------------------------------------------------------------------------------------------>

# Função que simula a preparação de pedidos


def preparar_pedidos(lista_a_fazer, lista_prontos):
    while lista_a_fazer:
        pedido_em_preparo = lista_a_fazer.pop(0)
        print(f"{pedido_em_preparo} está sendo preparado")
        lista_prontos.append(pedido_em_preparo)


pedidos_recebidos = ["Picanha", "Risoto", "Pizza"]
pedidos_preparados = []

# Antes
print(pedidos_recebidos)
print(pedidos_preparados)
preparar_pedidos(pedidos_recebidos, pedidos_preparados)

# Depois
print(pedidos_recebidos)
print(pedidos_preparados)

# ---------------//-----------------------
# Impedidndo que uma função modifique uma lista
pedidos_recebidos = ["Picanha", "Risoto", "Pizza"]
pedidos_preparados = []

# Antes
print(pedidos_recebidos)
print(pedidos_preparados)
preparar_pedidos(pedidos_recebidos[:], pedidos_preparados)

# Depois
print(pedidos_preparados)
print(pedidos_recebidos)

#------------------//------------------------


# Revisão positional arguments e keyword arguments


def mostra_nome_idade(nome, idade):
    print(f"{nome} tem {idade} anos")


mostra_nome_idade("potinho", 11)

# Keyword arguments
mostra_nome_idade(nome="potinho", idade="21")


# Como criar uma função que aceita qualquer números de argumentos (args e kwargs)

"""       Situação problema:
Crie uma função que receba os pedidos realizados em um site de vendas de roupas, e mostra o carrinho do cliente, isto é, uma lista com tudo que o cliente clicou para comprar.
"""


def mostrar_carrinho(*roupas):
    """ Imprime a lista de roupas no carrinho do cliente """
    for roupa in roupas:
        print(roupa)


mostrar_carrinho("Camiseta M", "Sueter G", "Tênis")


"""       Situação problema:
Crie uma função que recebe o nome do cliente e os pedidos realizados por este em um site de vendas de roupas. A função deverá imprimir o nome do cliente e uma lista com tudo que o cliente clicou para comprar.
"""


def mostrar_carrinho(nome, *args):
    """ Imprime a lista de roupas no carrinho do cliente """
    print(f"Carrinho do(a) {nome}:")
    for roupa in args:
        print(roupa)


mostrar_carrinho("potinho", "Camiseta", "Bermuda")
mostrar_carrinho("joão", "Bota", "luva", "calça", "short")

'''
""" Situação problema
Crie uma função que recebe dados de cadstro de um usuário. A função deverá receber obrigatoriamente o seu nome telefone. Mas pode receber quaisquer outros dados conhecidos do usuário
(endereço, email, idade, sexo, CPF, RG, etc)
"""


def criar_usuario(nome, telefone, **kwargs):  # se sobrar argumentos vai para **kwargs
    kwargs['nome'] = nome
    kwargs['telefone'] = telefone
    return kwargs


criar_usuario("potinho", 12345678, CPF=1232323232,
              RG=4242424242, email="potinho@gmail.com", sexo="M")

criar_usuario("potinho", 12345678)
