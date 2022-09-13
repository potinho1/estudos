""" Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor."""


lista = []
quadrado = 0

for i in range(10):
    quadrado += int(input(f"Número {i+1}: ")) ** 2
    lista.append(quadrado)

print(f"A soma dos quadrados dos elementos do vetor: {quadrado}\n")
print(f"A lista: {lista}")
