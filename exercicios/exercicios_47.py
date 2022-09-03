""" Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

alunos = 10
lista = []
media_7 = []
cont = 0


for i in range(alunos):
    cont += 1
    print(f"Aluno: {cont}")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    lista.append(media)
    print(lista)
    if media >= 7.0:
        media_7.append(media)
print(f"Teve {len(media_7)} alunos com media 7")
