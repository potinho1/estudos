# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.


nota1 = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite outra nota do aluno: "))

media = nota1 + nota2

if media < 9:
    print("Aprovado")
elif media <= 6:
    print("Reprovado")
elif media == 10:
    print("Parabéns tirou 10!")
