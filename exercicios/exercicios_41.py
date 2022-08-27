"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""

participacao = 0
perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]

for pergunta in perguntas:
    print(pergunta)
    resp = (input("Responda com sim ou não: ")).lower().replace('ã', 'a')
    if resp == 'sim':
        participacao += 1

if participacao == 2:
    print("Suspeita")

elif participacao == 3 or participacao == 4:
    print("Cúmplice")

elif participacao == 5:
    print("Assasino")

else:
    print("Inocente")
