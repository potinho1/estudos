from contato import Contato


class MinhaAgenda:
    """ Representa uma agenda de contatos telefônicos"""

    def __init__(self, contatos_dict=[]):
        """ Inicializa os atributos da agenda"""
        self.contatos = []
        if contatos_dict:
            for contato_dict in contatos_dict:
                contato = Contato(
                    contato_dict['nome'], contato_dict['telefone'])
                self.contatos.append(contato)
        self.contatos_dict = []

    def ver_contatos(self):
        """ Mostra a lista de contatos"""
        if self.contatos:
            print("\nLISTA DE CONTATOS\n")
            for pos, contato in enumerate(self.contatos):
                print(f"{pos}: {contato.nome}, {contato.telefone}")
            print("\n")
        else:
            print("Não há contatos armazenados na agenda. \n")

    def adicionar_contato(self):
        """ Cria um novo contato para ser adicionado á lista contatos"""
        print("\nNOVO CONTATO\n")
        nome = input("Insira o nome do novo contato: ")
        telefone = input("Insira o telefone do novo contato: ")
        novo_contato = Contato(nome.title(), telefone)
        self.contatos.append(novo_contato)
        self.contatos.sort(key=lambda contato: contato.nome)
        print("Contato adicionado com sucesso.\n")

    def excluir_contato(self):
        """ Exlcui um contato de acordo com sua posição"""
        if self.contatos:
            # Mostra a lista de contatos para que o usuário saiba qual contato ele quer excluir
            self.ver_contatos()

            # Solicita a posição do contato que o usuário deseja excluir
            pos = int(
                input("Informa a posição do contato que você deseja apagar: "))

            contato_exluido = self.contatos.pop(pos)

            print(f"{contato_exluido.nome} foi removido da lista contatos.\n")
        else:
            print("Não a contatos armazenados na agenda.\n")

    def editar_contato(self):
        """ Edita dados de um contatos"""

        if self.contatos:
            # Mostra a lista de contatos para que o usuário saiba a posição do contato que ele deseja editar
            self.ver_contatos()

            # Solicita a posição para o usuáiro do programa
            pos = int(
                input("Informa a posição do contato que você deseja editar: "))

            # Armazena o contato a ser editado na variavel contato_editado
            contato_editado = self.contatos[pos]

            # Mostra os dados atuais do contato a ser editado
            contato_editado.info()

            # Editar a informações do contato
            contato_editado.editar_nome()
            contato_editado.editar_telefone()

            # Mostra informações atualizadas do contato
            print("Informações atualizadas")
            contato_editado.info()

        else:
            print("Não há contatos armazenados na agenda.\n")

    def criar_contatos_dict(self):
        for contato in self.contatos:
            contato_dict = contato.__dict__
            self.contatos_dict.append(contato_dict)

    def run(self):
        """ Inicia a operação da agenda"""
        print("MINHA AGENDA")
        while True:
            print("1-Ver contatos | 2-Adiconar | 3-Excluir | 4-Editar | 5-Sair")
            comando = input("Digite o comando desejado: ")
            if comando in ["1", "2", "3", "4", "5"]:
                if comando == "1":
                    self.ver_contatos()
                elif comando == "2":
                    self.adicionar_contato()
                elif comando == "3":
                    self.excluir_contato()
                elif comando == "4":
                    self.editar_contato()
                else:
                    print("Até a próxima!")
                    self.criar_contatos_dict()
                    break
            else:
                print("Insira um comando válido!\n")
