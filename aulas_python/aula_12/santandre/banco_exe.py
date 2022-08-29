from contas_ficticias import contas
from santandre import BancoSantandre

banco_santandre = BancoSantandre(contas)

while True:
    print("O que você deseja fazer?")
    print("1-criar conta | 2-Mostrar contas | 3-Ver totais | 4-sair")
    comando = input("Digite o comando desejado (1/2/3/4): ")
    if comando not in ["1", "2", "3", "4"]:
        print("Comando inválido\n")
    elif comando == "1":
        banco_santandre.criar_conta_pf()
    elif comando == "2":
        banco_santandre.mostrar_contas()
    elif comando == "3":
        banco_santandre.total()
    else:
        print("Obrigado e até a próxima")
        break
