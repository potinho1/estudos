'''my_list = [1, 2, 3, 4, 5, ]
comidas = ['pizza', 'churrasco', 'hotdog']

print(my_list[2])
print(comidas)

lista_de_listas = [my_list, comidas]

print(lista_de_listas[0][1])


# imprimir a lista como tabela usa o for
identidade = [[1, 0], [0, 1]]

for i in identidade:
    print(i)


# Pode somar para achar um elemento da lista:
my_lista = [1, 2, 3, 4]
i = 2
print(my_lista[i+1])


# Alterar um campo na lista

lista = [1, 4, 6, 10, 12, 23]

lista[1] = 3

print(lista)


# Saber quantos elementos tem na sua lsita

lista = [1, 2, 3, 4, 5]

print(len(lista))


# Adicionar elementos dentro da lista

lista = [1, 2, 3, 4]

lista.append(5)

print(lista)


# Adicionar um elemento em um lugar especifico da lista

lista = [1, 2, 3, 4]

lista.insert(0, 0)

print(lista)


# Remover um elemento da lista

lista = [1, 2, 3, 4, ]

del lista[0]

print(lista)


# Remover um elemento da lista depois que você usar ele

lista = [1, 2, 3, 4]

lista.pop(0)

print(lista)
-------------
lista = [1, 2, 3, 4]
print(lista)
print(f"O pedido {lista.pop(1)} está pronto")
print(lista)


# Remover elemento pelo valor, aqui não importa qual o lugar dele ele remove o elemento que coloca nas ()

lista = [1, 2, 3, 4]

lista.remove(1)

print(lista)


# Combinar lista
lista_1 = [1, 2, 3, 4]
lista_2 = [5, 6, 7, 8]

lista_1.extend(lista_2)

print(lista_1)


# Organicar listas
lista = [1, 3, 2, 4]

lista.sort()  # Classifica a lista em ordem crescente por padrão.
print(lista)

# Organizar listas
lista = [1, 2, 3, 4, 4, 5]

print(lista)
lista.sort(reverse=True)
print(lista)


# Organizar listas temporariamente
lista = [1, 3, 4, 2]

print(sorted(lista, reverse=True))


# Inverter a ordem da lista
lista = [1, 2, 4, 5, 7]

print(lista)
lista.reverse()
print(lista)
'''
