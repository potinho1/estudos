""" Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""

nota_float = []
notas = []


while True:
    valor = input("Digite um valor: ")
    notas.append(valor)
    if valor == '-1':
        notas.remove('-1')
        break

print(f"Foram lidos {len(notas)} números.")
print("-" * 30)
print(f"Lista na ordem informado: {notas}")
print("-" * 30)
notas.reverse()
print(f"Lista inversa: {notas}")
print("-" * 30)

# Transdormando a lista str em float
for nota_i in notas:
    nota_float.append(float(nota_i))
print(type(nota_float[0]))
print("-" * 30)

# Calcule e mostre a soma dos valores
soma = 0
for nota in nota_float:
    soma += nota
print(f"A soma dos valores da lista: {soma}")
print("-" * 30)

# Calcule e mostre a média dos valores
media = soma/len(nota_float)
print(f"A media é {media:.2f}")
print("-" * 30)

# Calcule e mostre a quantidade de valores acima da média calculada
acima_media = 0
for nota in nota_float:
    if nota > media:
        acima_media += 1
print(f"{acima_media} Valores a cima da media.")
print("-" * 30)
# Calcule e mostre a quantidade de valores abaixo de sete
abaixo_7 = 0
for nota in nota_float:
    if nota < 7:
        abaixo_7 += 1
print(f"{abaixo_7} Valores a baixo da media.")
print("-" * 30)

print("Programa encerrado!!")
