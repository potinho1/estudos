# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input("Quantos graus esta fazendo? "))

f = c * (9 / 5) + 32
print(f"Esta fazendo {f:.0f} F")
