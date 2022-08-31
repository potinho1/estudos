class Contato:
    """ Representa um contato"""

    def __init__(self, nome, telefone):
        """ Atributos"""
        self.nome = nome
        self.telefone = telefone

    def info(self):
        """ Mostra as informações do contato"""
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")

    def editar_nome(self):
        """ Edita o valor associado com o atributo nome do contato"""
        novo_nome = input(
            "Entre com o novo nome do contato (ENTER para mnater o nome atual): ")
        if novo_nome != "":
            self.nome = novo_nome.title()
            print("Nome alterado com sucesso!")

    def editar_telefone(self):
        """ Edita o valor associado com o atributo telefone nome do contato"""
        novo_tel = input(
            "Entre com o novo telefone do contato (ENTER para mnater o telefone atual): ")
        if novo_tel != "":
            self.telefone = novo_tel
            print("Telefone alterado com sucesso!")
