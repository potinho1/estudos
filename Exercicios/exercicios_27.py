"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280, 00 (incluindo): aumento de 20%
    salários entre R$ 280, 00 e R$ 700, 00: aumento de 15%
    salários entre R$ 700, 00 e R$ 1500, 00: aumento de 10%
    salários de R$ 1500, 00 em diante: aumento de 5 % Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""

from time import sleep

salario_colaborador = float(input("Qual o valor do seu salario? "))

aumento_20 = salario_colaborador * 0.20
aumento_15 = salario_colaborador * 0.15
aumento_10 = salario_colaborador * 0.10
aumento_5 = salario_colaborador * 0.05

if salario_colaborador <= 280:
    print(f"O salário antes do reajuste R${salario_colaborador}")
    print("Calculando....")
    sleep(5)
    print(f"Aumentou: R${aumento_20}")
    print(f"O novo saláiro: R${aumento_20 + salario_colaborador}")


elif salario_colaborador > 280 and salario_colaborador <= 700:
    print(f"O salário antes do reajuste R${salario_colaborador}")
    print("Calculando....")
    sleep(3)
    print(f"Aumentou: R${aumento_15}")
    print(f"O novo saláiro: R${aumento_15 + salario_colaborador}")

elif salario_colaborador > 700 and salario_colaborador <= 1500:
    print(f"O salário antes do reajuste R${salario_colaborador}")
    print("Calculando....")
    sleep(5)
    print(f"Aumentou: R${aumento_10}")
    print(f"O novo saláiro: R${aumento_10 + salario_colaborador}")

elif salario_colaborador > 1500:
    print(f"O salário antes do reajuste R${salario_colaborador}")
    print("Calculando....")
    sleep(5)
    print(f"Aumentou: R${aumento_5}")
    print(f"O novo saláiro: R${aumento_5 + salario_colaborador}")
