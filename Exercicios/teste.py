"""alunos = []


def cadastro_alunos(nome, idade, turma, doenca=[]):
    aluno = {
        'nome': nome,
        'idade': idade,
        'turma': turma,
        'doença': doenca
    }
    return aluno


def mostrar_alunos():
    for aluno in alunos:
        print(f"Nome do aluno: {aluno['nome']}")
        print(f"Nome do aluno: {aluno['idade']}")
        print(f"Nome do aluno: {aluno['turma']}")
        if aluno['doença']:
            print("Doenças do aluno:")
            for doenca in aluno['doença']:
                print(f"\t{doenca}")
        print("-" * 20)
        print()


def cadastrar_aluno():
    while True:
        resposta_nome = str(input("Informe seu nome: "))
        resposta_idade = int(input("Informe sua idade: "))
        resposta_turma = input("Informe sua turma: ")
        teste_doenca = str(input("O aluno tem alguma doença? (S/N)")).lower()
        if teste_doenca == 's':
            lista_doenca = []
            while True:
                tipo_doenca = str(
                    input("Infome a doença: ('n' para finalizar as doenças)")).lower()
                if tipo_doenca == 'n':
                    break
                lista_doenca.append(tipo_doenca)
            aluno = cadastro_alunos(resposta_nome, resposta_idade,
                                    resposta_turma, teste_doenca)
        else:
            aluno = cadastro_alunos(
                resposta_nome, resposta_idade, resposta_turma)
            alunos.append(aluno)
        continuar = input("Deseja cadastrar mais algum aluno? (S/N)").lower()
        print()
        if continuar == 'n':
            break


cadastrar_aluno()
mostrar_alunos()
"""


# Email


class Email:
    def __init__(self, nome, resumo, destino):
        self.nome = nome
        self.resumo = resumo
        self.destino = destino


primeiro_email = Email("Potinho", "Olá, seja bem vindo", "potinho@gmail.com")

print(primeiro_email.nome)
print(primeiro_email.resumo)
print(primeiro_email.destino)
