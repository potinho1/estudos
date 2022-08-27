from cliente import PessoaFisica as PF
from conta import ContaCorrente as CC

pessoa_fisica_var = PF("Potinho", 34354354565, "potinho@gmail.com")
conta_corrente_var = CC(pessoa_fisica_var, 123456)


print(f"Seja bem vindo, {conta_corrente_var.cliente.nome}!\n\n")


while True:
    print("O que você deseja fazer? ")
    print("1-Depósitar  |  2-Sacar  |  3-Ver extrato  |  4-Finalizar")
    comando = input("Digite um comando (1|2|3|4): ")

    # Testar se o comando é válido
    if comando not in ['1', '2', '3', '4']:
        print("Comando inválido/n")
        continue

    elif comando == '1':
        deposito = int(input("Informe o valor de depósito: "))
        conta_corrente_var.depositar(deposito)

    elif comando == '2':
        saque = int(input("Informe o valor do saque: "))
        conta_corrente_var.sacar(saque)

    elif comando == '3':
        operacoes = int(input("Informe a quantidade que você quer ver: "))
        conta_corrente_var.ver_extrato(operacoes)

    elif comando == '4':
        break
