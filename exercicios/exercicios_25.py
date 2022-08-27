# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for n in range(3):
    n = int(input("Digite um número: "))
    lista.append(n)
    lista.sort(reverse=True)
print("-" * 30)
print(lista)
print("-" * 30)
for listas in lista:
    print(f"Ordem decrescente: {listas}")
