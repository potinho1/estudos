from cliente import PessoaFisica
from conta import ContaCorrente


class BancoSantandre:
    """ Classe para representar o Banco Santandre"""

    def __init__(self, contas=[]):
        """ Inicializa os atributos do Banco"""
        self.contas = contas

    def criar_conta_pf(self):
        """ Cria uma nova conta para pessoa física e adiciona na lista associada com o atributo contas"""
        nome = input("Infome o nome do cliente: ")
        cpf = input("Informe o CPF do cliente: ")
        email = input("Informe o email do cliente: ")
        cliente = PessoaFisica(nome, cpf, email)
        num_conta = input("Infome o número da conta: ")
        self.contas.append(ContaCorrente(cliente, num_conta))
        print("\n")

    def mostrar_contas(self):
        """ Mostra informações de todas as contas"""
        for conta in self.contas:
            print(f"CONTA: {conta.num_conta}")
            conta.cliente.info()
            conta.ver_extrato(3)
        print("\n")

    def total(self):
        """ Mostra o valor total gerenciado pelo banco"""
        total = 0
        for conta in self.contas:
            total += conta.saldo
        print(f"O banco gerencia atualmente {total}R$\n")
