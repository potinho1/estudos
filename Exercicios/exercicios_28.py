""" 
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220

     Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

"""


valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou esse mês? "))

salario_brunto = (valor_hora * horas_trabalhadas)

if salario_brunto <= 900:
    desconto = 0

elif salario_brunto <= 1500:
    desconto = 5

elif salario_brunto <= 2500:
    desconto = 10

else:
    desconto = 20


IR = salario_brunto * (desconto / 100)
INSS = salario_brunto * (10 / 100)
FGTS = salario_brunto * (11 / 100)
total_desc = IR + INSS
salario_liquido = salario_brunto - total_desc

print(
    f"\nSalário Bruto: {salario_brunto:.2f}",
    f"\nIR (5%): {IR:.2f}",
    f"\nINSS (10%): {INSS:.2f}",
    f"\nFGTS (11%): {FGTS:.2f}"
    f"\nTotal de descontos: {total_desc:.2f}"
    f"\nSalário Liquido: {salario_liquido:.2f}"
)
