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

num_vendedores = int(input('Quantos vendedores a loja tem? '))

salarios = []
classe = []
for vendedor in range(1,num_vendedores+1):
    vendas = float(input('\nQuanto o vendedor '+str(vendedor)+' arrecadou essa semana? '))
    salarios.append(200+(vendas*0.09))

dicionario = {'1':[range(200,300),0],'2':[range(300,400),0],
              '3':[range(400,500),0],'4':[range(600,700),0],
              '5':[range(700,800),0],'7':[range(800,900),0],
              '8':[range(900,1000),0],'9':[range(1000,100000),0]}  

#dicionario.keys() - pega o valor das chaves de cada dicionário

for salario in salarios:
    print(salario)
    for idx in dicionario.keys():
        print(idx)
        if salario in dicionario[idx][0]:
            classe.append(idx)
            dicionario[idx][1] = dicionario[idx][1] + 1     
            
#for idx in dicionario.keys():
#    inicial = dicionario[idx][0][0]
#    final = dicionario[idx][0][-1]
#    quant = dicionario[idx][1]
#    if final == 99999:
#        print('Número de funcionários com salário acima de R$1000,00 iguai a '+str(quant))
#    else:
#        print('Nuúmero de funcionários com salário de R$'+str(inicial)+ ' a R$'+str(final)+' igual a: '+str(quant))