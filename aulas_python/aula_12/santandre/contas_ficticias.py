from cliente import PessoaFisica
from conta import ContaCorrente

cliente1 = PessoaFisica("Potinho", 999899, "potinho@gmail.con")
conta1 = ContaCorrente(cliente1, 1234456, 5000, [-50, 40, 10, 1000])

cliente2 = PessoaFisica("Potinho", 999899, "potinho@gmail.con")
conta2 = ContaCorrente(cliente2, 1234456, 5000, [5, 40, 10, 1000])


cliente3 = PessoaFisica("Potinho", 999899, "potinho@gmail.con")
conta3 = ContaCorrente(cliente3, 1234456, 5000, [-50, 40, 10, 1000])


cliente4 = PessoaFisica("Potinho", 999899, "potinho@gmail.con")
conta4 = ContaCorrente(cliente4, 1234456, 5000, [-50, 40, 10, 1000])

contas = [conta1, conta2, conta3, conta4]
