"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. """
'''

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

---------------------------------------------------->
'''

idades = []
alturas = []


for i in range(30):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    idades.append(idade)
    alturas.append(altura)
    mediaAltura = sum(alturas)/len(alturas)
    quantidadeAlunos = 0
    for i in range(0, len(idades)):
        if idades[i] > 13 and alturas[i] < mediaAltura:
            quantidadeAlunos = quantidadeAlunos + 1

print(
    f"Alunos que possuem mais de 13 anos e altura inferior são: {quantidadeAlunos}")
