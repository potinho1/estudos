with open('C:/Users/gomes/OneDrive/Área de Trabalho/Estudos-Python/Scripts/Aulas Python/aula_14/Manipulando Arquivos/compositores.txt') as f:
    for linha in f:
        print(linha.rstrip())

"""
#Sem o loop

linhas = f.readlines()
print(linhas[2])

"""
