""" Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""


num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

resp = str(input("Qual operação deseja fazer: (+ - * /): "))


def checar():
    if (resultado // 1 == resultado):
        print("Inteiro")
        if resultado % 2 == 0:
            print("Par")
            if resultado > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Ímpar")
    else:
        print("Decimal")


if resp == '+':
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} = {resultado}")
    checar()

elif resp == '-':
    resultado = num1 - num2
    print(f"A subtração de {num1} e {num2} = {resultado}")
    checar()

elif resp == '*':
    resultado = num1 * num2
    print(f"A multiplicação de {num1} e {num2} = {resultado}")
    checar()

elif resp == '/':
    resultado = num1 / num2
    print(f"A divisão de {num1} e {num2} = {resultado}")
    checar()

else:
    print("Operação inválida")
