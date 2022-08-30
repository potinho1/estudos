# Aula 7: Função input() e loop while
'''
print('=' * 20)
print("Faça a sua escolha:")
print('=' * 20)
pilula = str(input("Qual a cor da pílula que você deseja tomar? ")
             ).lower()  # prompt
if pilula == 'azul':
    print("Pode voltar para o seu mundo de mentiras.")
elif pilula == 'vermelho':
    print("Venha comigo! Vou te mostrar a verdade sobre matrix")
else:
    print(f"Desculpe estamos sem {pilula}")

------------------------------------------------------------------ ->

# Posso tirar a CNH

print("Descubra se pode tirar a a sua CNH")

usuario = int(input("Qual a sua idade? "))
print(f"Você tem {usuario} anos")

if usuario >= 18:
    print("Pode tirar a CNH")
else:
    print("Desculpe!")
    print("Você não pode tirar a CNH")

--------------------------------------->

# Loop 1 a 10
numero = 1

while numero <= 10:
    print(numero)
    numero += 1  # numero = numero + 1
----------------------------------------->


# Repetir ate um sinal

print("Descubra se pode tirar a a sua CNH\n")

usuario = int(
    input("Qual a sua idade? Entre com o 0 para finalizar o programa "))
while usuario != 0:
    print(f"Você tem {usuario} anos")
    if usuario >= 18:
        print("Pode tirar a CNH")
    else:
        print("Desculpe!")
        print("Você não pode tirar a CNH")
    usuario = int(
        input("Qual a sua idade? Entre com o 0 para finalizar o programa "))

-------------------------------------------------------------------------------->

# Revisado com flag
print("Descubra se pode tirar a a sua CNH\n")

programa_ativo = True

while programa_ativo:
    usuario = int(
        input("Qual a sua idade? Entre com o 0 para finalizar o programa "))
    if usuario == 0:
        programa_ativo = False
    else:
        print(f"Você tem {usuario} anos")
        if usuario >= 18:
            print("Pode tirar a CNH")
        else:
            print("Desculpe!")
            print("Você não pode tirar a CNH")

--------------------------------------------------->

# Saindo se um loop com o comando break
# O comando break controla o fluxo do seu programa. Através dele é possivel sair imediatamente de um loop.

print("Descubra se pode tirar a a sua CNH\n")

usuario = int(
    input("Qual a sua idade? Entre com o 0 para finalizar o programa "))
while True:
    if usuario == 0:
        break
    print(f"Você tem {usuario} anos")
    if usuario >= 18:
        print("Pode tirar a CNH")
    else:
        print("Desculpe!")
        print("Você não pode tirar a CNH")
    usuario = int(
        input("Qual a sua idade? Entre com o 0 para finalizar o programa "))

--------------------------------------------------->

# Indo para a proxima iteração através do comando continue
# O comando continue permite saltar diretamente apara próxima repetição de um loop de acordo com determinadas condições.

alunos_rec = [2, 5, 14, 26, 30, 31, 32, 33, 39]

aluno = 1

while aluno <= 40:
    if aluno in alunos_rec:
        aluno += 1
        continue
    print(f"O aluno de número {aluno} irá ao passeio")
    aluno += 1
--------------------------------------------------->
'''
