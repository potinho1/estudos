""""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. """

gasolina = 2.5
alcool = 1.9

tipo_combustivel = str(input("A-álcool G-gasolina: ")).upper()

if tipo_combustivel == 'A':
    pergunta = int(input("Quantos litros de álcool deseja colocar? "))
    if pergunta <= 20:
        soma_litros = (pergunta * alcool)
        desconto = (soma_litros * 0.04) - soma_litros
        print(f"Total a pagar {desconto}")
    elif pergunta > 21:
        soma_litros = (pergunta * alcool)
        desconto = (soma_litros * 0.06)
        valor = desconto - soma_litros
        print(f"Total a pagar {valor}")

if tipo_combustivel == 'G':
    pergunta = int(input("Quantos litros de gasolina deseja colocar? "))
    if pergunta <= 20:
        soma_litros = (pergunta * gasolina)
        desconto = (soma_litros * 0.03) - soma_litros
        print(f"Total a pagar {desconto}")
    elif pergunta > 21:
        soma_litros = (pergunta * gasolina)
        desconto = (soma_litros * 0.05)
        valor = desconto - soma_litros
        print(f"Total a pagar {valor}")
