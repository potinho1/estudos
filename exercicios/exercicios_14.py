# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

from time import sleep

regularmento = 50
multa = 4

pescador = float(input("Quantos kilos de peixe você pescou? "))

if pescador >= 51:
    execesso = pescador - regularmento
    print(f"Você execedeu {execesso:.0f} kilos de peixe")
    print("Calculando quanto vai pagar de multa...")
    sleep(5)
    pagar_multa = execesso * multa
    print(f"Total a pagar {pagar_multa:.2f} reias")
elif pescador <= 50:
    print("Obrigado por pescar com a gente, você não precisa pagar multa!")
    print("Até a proxima!!")
