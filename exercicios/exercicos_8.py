# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
from time import sleep

mes = 30

ganho_hora = float(input("Quanto você ganha por hora? "))
hora_trabalhada = int(input("Qantas horas você trabalha? "))

salario = ganho_hora * hora_trabalhada
ganho_mes = mes * salario

print("Estamos calculando...")
sleep(3)

print(f"Seu salario nesse mes foi R${int(ganho_mes)},00")
