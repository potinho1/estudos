""" Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
 Imprima a idade e a altura na ordem inversa a ordem lida."""


idades = []
altura = []
pessoa = 0

for i in range(0, 5):
    pessoa += 1
    print(f"Pessoa {pessoa}")
    idade = int(input("Qual a sua idade: "))
    alt = float(input("Qual a sua altura: "))
    idades.append(idade)
    altura.append(alt)


print(idades)
print(altura)
print("Inverso\n")

idades.reverse()
print(idades)
altura.reverse()
