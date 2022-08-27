alunos = []


def criar_aluno(nome, idade, turma, doencas=[]):
    aluno_dict = {
        'nome': nome,
        'idade': idade,
        'turma': turma,
        'doenças': doencas
    }
    return aluno_dict

# {'nome': valor, 'idade':valor, 'turma':valor, 'doenças':[]}


def mostrar_alunos():
    for aluno in alunos:
        print(f"Nome do aluno: {aluno['nome']}")
        print(f"Idade do aluno: {aluno['idade']}")
        print(f"Turma do aluno: {aluno['turma']}")
        if aluno['doenças']:
            print("Doeças do aluno: ")
            for doenca in aluno['doenças']:
                print(f"\t{doenca}")
        print("_" * 30)
        print()


def cadastrar_alunos():
    while True:
        resposta_nome = str(input("Informe o nome do aluno: "))
        resposta_idade = int(input("Infome a idade do aluno: "))
        resposta_turma = input("Informe a turma do aluno: ")
        tem_doenca = input("O aluno tem alguma doença? (S/N): ").lower()
        if tem_doenca == 's':
            lista_doencas = []
            while True:
                resposta_doenca = input(
                    "Informe a doença do aluno (para finalizar entre com 'f'): ").lower()
                if resposta_doenca == 'f':
                    break
                lista_doencas.append(resposta_doenca)
            aluno = criar_aluno(resposta_nome, resposta_idade,
                                resposta_turma, resposta_doenca)
        else:
            aluno = criar_aluno(resposta_nome, resposta_idade, resposta_turma)
            alunos.append(aluno)
        continuar = input(
            "Para cadastrar mais um aluno entre com 'a': ").lower()
        print("-" * 50)
        if continuar != 'a':
            break


cadastrar_alunos()
mostrar_alunos()
