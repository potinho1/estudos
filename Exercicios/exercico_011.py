# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
num_real = float(input("Digite um número real: "))

print('Soma:', ((2*num_1) + (num_2/2)))
print('Produto:', (3 * num_1) + num_real)
print('Cubo:', num_real**3)
