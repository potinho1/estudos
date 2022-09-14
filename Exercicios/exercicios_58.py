#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
#O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
#Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
#Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

salario_funcionario = float(200)
cont = 0
colaboradores = int(input('Quantos colaboradores tem: '))

for i in range(colaboradores):
    vendas_semana = float(input('Digite o valor de faturamento da semana: '))

    total_porcento = (vendas_semana * 9) / 100

    total_salario = total_porcento + salario_funcionario

    if total_salario >= 200 or total_salario >= 299:
        cont += 1
        print(f'Colaboradore {cont} recebeu {total_salario}')

