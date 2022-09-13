# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia_semana = int(input(
    "Digite um núemero para saber qual o dia da semana (1-Domingo, 2- Segunda, etc.): "))

if dia_semana == 1:
    print("Domingo")

elif dia_semana == 2:
    print("Segunda-feira")

elif dia_semana == 3:
    print("Terça-feira")

elif dia_semana == 4:
    print("Quarta-feira")

elif dia_semana == 5:
    print("quinta-feira")

elif dia_semana == 6:
    print("Sexta-feira")

elif dia_semana == 7:
    print("Sabado")

else:
    print("Número inválido!")
