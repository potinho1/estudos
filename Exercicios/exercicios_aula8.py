# Lista de alunos

# Vamos criar uma lista chamada alunos que armazenará dados de diversos alunos através de dicionários que possuem as seguintes chaves: 'nome', 'idade' e 'turma'


alunos = []


def criar_aluno(nome, idade, turma):
    aluno_dict = {
        'nome': nome,
        'idade': idade,
        'turma': turma
    }
    return aluno_dict


aluno1 = criar_aluno("potinho", 14, "2c")
aluno2 = criar_aluno("ana", 12, "1c")

print(aluno2)
