# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Qual o seu sexo? (F/M)")).lower()

if sexo == 'm':
    print("Você é do sexo Masculino!")

elif sexo == 'f':
    print("Você é do sexo Feminino!")

else:
    print("Sexo inválido!")
