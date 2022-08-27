# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Digite o preço do primerio produto: "))
preco2 = float(input("Digite o preço do primerio produto: "))
preco3 = float(input("Digite o preço do primerio produto: "))

if preco1 < preco2 and preco1 < preco3:
    print(f"Compre o produto {preco1} ele está mais barato")
elif preco2 < preco1 and preco2 < preco3:
    print(f"Compre o produto {preco2} ele está mais barato")
elif preco3 < preco1 and preco3 < preco2:
    print(f"Compre o produto {preco3} ele está mais barato")
