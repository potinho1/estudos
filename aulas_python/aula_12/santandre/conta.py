class ContaCorrente:
    """ Classe para representar uma conta corrente"""

    def __init__(self, cliente, num_saldo, saldo=0, extrado=[]):
        """ Inicializa os atributos da conta corrente"""
        self.cliente = cliente
        self.num_saldo = num_saldo
        self.saldo = saldo
        self.extrato = extrado

    def depositar(self, deposito):
        """ Deposita uma quantidade no atributo saldo e registra na operação em extrato"""
        if deposito == 0:
            print("Valor inválido\n")
        else:
            saldo_inicial = self.saldo
            self.saldo += deposito
            self.extrato.append(self.saldo - saldo_inicial)
            print("Depósito efetuado com sucesso!\n")

    def sacar(self, saque):
        # Saca uma quantidade do aributo saldo e regista na operação extrato
        if saque == 0:
            print("Valor inválido\n")
        else:
            saldo_inicial = self.saldo
            self.saldo -= saque
            self.extrato.append(self.saldo - saldo_inicial)
            print("saque efetuado com sucesso!\n")

    def ver_extrato(self, operacao=0):
        """ Mostra o extrato da conta corrente"""
        print("Opereção    valor")
        print("_"*20)
        for operacao in self.extrato[-operacao:]:
            if operacao > 0:
                print(f"Depósito     {operacao}R$")
            else:
                print(f"Saque        {operacao}R$")
        print("_"*20)
        print(f"Total            {self.saldo}\n")
