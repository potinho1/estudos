class PessoaFisica:
    """ Classe para representar um cliente PF"""

    def __init__(self, nome, cpf, email):
        """ Inicializa os atributos do cliente PF"""
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def info(self):
        """ Mostra informações sobre o cliente PF"""
        print("-" * (18+len(self.nome)))
        print(f"Nome do cliente: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")
        print("-" * (18+len(self.email))+"\n")
