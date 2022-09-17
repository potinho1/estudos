"""#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
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

l = [0,0,0,0,0,0,0,0,0]
x=0

while True:
    n = float(input("Informe seu salário %dº R$:" %(x+1)))
    if 200 < n <299:
        l[0]+=1
    elif 300 < n > 399:
        l[1]+=1
    elif 400 < n > 499:
        l[2]+=1
    elif 500 < n > 599:
        l[3]+=1
    elif 600 < n > 699:
        l[4]+=1
    elif 700 < n > 799:
        l[5]+=1
    elif 800 < n > 899:
        l[6]+=1
    elif 900 < n > 999:
        l[7]+=1
    elif n >= 1000:
        l[8]=[8]+1
    x+=1
    d = input('deseja continuar?(s ou n)')
    if d == 'n':
        break
    print(l[0])

"""

Salário (n) = 200 + comissão
Lista = Salário em intervalos de 100 (0 ~99)​

Fórmula (caminho inverso do algoritmo do salário):

Índice do vetor = int ou piso [(salário - 200) ÷ 100]​