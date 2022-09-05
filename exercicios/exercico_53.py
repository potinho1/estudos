"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. """

from statistics import quantiles

idades = [18, 19, 20, 21, 22]
alturas = [1.80, 1.70, 1.90, 1.85, 1.99]

i = 0
soma = 0

while i < len(alturas):
    soma += alturas[i]
    i += 1

media = soma / len(alturas)

c = 0
quantidade = 0
while c < len(idades):
    if (idades[c] > 13 and alturas[c] < media):
        quantidade += 1
    c += 1
print(quantidade)
