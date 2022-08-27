""" 
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

morangos = float(input("Quantos kilo de morango? "))
maca = float(input("Quando kilos de maça? "))

preco_morango1 = morangos * 2.50
preco_morango2 = morangos * 2.20

preco_maca1 = maca * 1.80
preco_maca2 = maca * 1.50

print(f"Quantidades de morangos {morangos}\nQauntidade de maça {maca}")

if morangos > 5:
    preco_morango = preco_morango1

else:
    preco_morango = preco_morango2

if maca > 5:
    preco_maca = preco_maca1

else:
    preco_maca = preco_maca2

preco_total = preco_morango + preco_maca

if preco_total > 25 or (maca + morangos) > 8:
    print("Preço final:", (preco_total - (preco_total * 0.1)))

else:
    print(f"Preço final: {preco_total}")
