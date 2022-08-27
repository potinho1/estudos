# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# altura = float(input("Digite sua altura: ")

print("Calcule seu peso atual home ou mulher")

pergunta = int(input("Homem [1] ou Mulher [2]? "))

if pergunta == 1:
    altura_homem = float(input("Digite sua altura homem? "))
    peso_homem = (72.7 * altura_homem) - 58
    print(f"Seu peso ideal é aproximadamente é {peso_homem:.2f}")
elif pergunta == 2:
    altura_mulher = float(input("Digite sua altura mulher? "))
    peso_mulher = (62.1 * altura_mulher) - 44.7
    print(f"Seu peso ideal é aproximadamente é {peso_mulher:.2f}")
