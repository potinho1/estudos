""" Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se seu argumento for zero ou negativo"""


def PN(n):
    if n > 0:
        print("P")
    else:
        print("N")
    return n


PN(1)
PN(-199)
