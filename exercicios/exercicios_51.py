""" Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""


vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetor3 = []

intercalados = vetor1 + vetor2

intercalados[::2] = vetor1
intercalados[1::2] = vetor2
vetor3.append(intercalados)


print(f"Lista 1: {vetor1}")
print(f"Lista 2: {vetor2}")
print(f"Lista intercalados: {intercalados}")
