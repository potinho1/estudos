"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

numeros = 20
lista = []
pares = []
impares = []

for i in range(numeros):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nInteiros")
for numero in lista:
    print(f"{numero}", end=" ")

print("\nPares")
for numero in pares:
    print(f"{numero}", end=" ")

print("\nImpares")
for numero in impares:
    print(f"{numero}", end=" ")
