'''# Vamos criar um programa que simula o fluxo de um restaurante.
# O programa deverá possuir duas listas, uma será uma lista de pedidos prontos e outra de pedidos não prontos, ambas começam vazias.
# Através de um loop, vamos inserir itens de pedidos não prontos.
# Depois que todos os pedidos forem realizados, vamos simular a preparação dos pedidos movendo os itens da lista de pediso não prontos para a lista de pedidos prontos.
# Á medida em que os pedidos são preparados, mostramos uma mensagem informando qual pedido ficoi pronto.
# Repetimos todo esse fluxo até quando o comando "fechar restaurante" seja passado ao programa

# Restaurante simulater

pedidos_prontos = []
pedidos_nao_prontos = []

while True:
    pedido = str(
        input("Informe o seu pedido. (entre com 'fp' para finalizar) "))
    if pedido == 'fp':
        break
    pedidos_nao_prontos.append(pedido)

print("\nA preparar: ")
for pedido in pedidos_nao_prontos:
    print(pedido)

# Preparando pedidos
while pedidos_nao_prontos:
    pedido_atual = pedidos_nao_prontos.pop(0)

    pedidos_prontos.append(pedido_atual)
    print(f"O pedido {pedido_atual} ficou pronto!")

print(pedidos_nao_prontos)
print(pedidos_prontos)


# Apartir de uma lista l, que pode ou não ter itens repetidos, pergunte ao usuário qual item ele quer apagar da lista e remova todas as instâncias desse item.

l = []

enchendo_lista = True

while enchendo_lista:
    item = input(
        "Qual valor você deseja inserir na lista? (entre com 'sair' para finalizar) ")
    if item == 'sair':
        enchendo_lista = False
    else:
        l.append(item)

print("\nSua lista ficou assim:")
print(l)

excluido = input("\nQual valor voce quer remover da lista? ")


while excluido in l:
    l.remove(excluido)


print("\nSua lista ficou assim:")
print(l)

--------------------------------------------------------------------->
'''
clientes = {}

dados = ['email', 'telefone']

print("=" * 20)
print("CADASTRO DE CLIENTE\n")
print("=" * 20)

while True:
    cliente = str(input("Informe do nome do cliente: "))
    clientes[cliente] = {}
    for dado in dados:
        resposta = input(f"Informe o {dado} do cliente: ")
        clientes[cliente][dado] = resposta
    continuar = input(
        "Para cadastrar mais um cliente digite 's'. Para finalizar entre com qualquer outro valor").lower()
    if continuar != 's':
        break
