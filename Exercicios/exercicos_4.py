# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Digite uma nota: "))
nota2 = int(input("Digite outra nota: "))
nota3 = int(input("Digite mais uma nota: "))
nota4 = int(input("Digite a ultima nota: "))

nota_final = nota1 + nota2 + nota3 + nota4
valor_final = nota_final / 2

print(f"A media final do aluno foi {valor_final}")
