"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa
"""


lista = []

for i in range(10):
    lista.append(float(input("Número: " + str(i) + ':')))
print(lista)
lista.reverse()
print(lista)
print("\n")
