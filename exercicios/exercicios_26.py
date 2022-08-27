# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("=" * 25)
print("M-matutino = Manhã")
print("V-vesoertino = Tarde")
print("N=noturno = Noite")
print("=" * 25)


turno = str(input("Que turno você estuda? ")).upper()

if turno == 'M' or turno == 'm':
    print("Bom dia!")
elif turno == 'V' or turno == 'v':
    print("Boa tarde!")
elif turno == 'N' or turno == 'n':
    print("Boa noite!")
else:
    print("Valor inválido!")
