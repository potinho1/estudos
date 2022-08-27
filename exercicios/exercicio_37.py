""" Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

print("-" * 20)
print("Sacar de 10 a 600")
print("-" * 20)

num = int(input("Quanto deseja sacar? "))

cem = int(num / 100)
num -= (cem*100)

cinquenta = int(num / 50)
num -= (cinquenta*50)

dez = int(num / 10)
num -= (dez * 10)

cinco = int(num / 5)
num -= (cinco * 5)

um = num

print("Notas R$100: ", cem)
print("Notas R$50: ", cinquenta)
print("Notas R$10: ", dez)
print("Notas R$5: ", cinco)
print("Notas R$1: ", um)
