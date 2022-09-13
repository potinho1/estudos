# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9) T(°C) = (T(°F) - 32) × 5/9

temperatura = float(input("Quantos graus esta fazendo? "))

C = (temperatura - 32) * (5 / 9)

print(f"A temperatua em celsius é {int(C)}C")
