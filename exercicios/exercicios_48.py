""" Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

interios = []

for i in range(0, 5):
    num = int(input("Digite um número: "))
    soma = num + num + num + num + num
    multiplicacao = soma * 5
    interios.append(num)

print(f"A soma de {num} + {num} + {num} + {num} é = {soma}")
print(f"A multiplicação de {soma} * 5 é = {multiplicacao}")
print(f"Números digitados: {interios}")
