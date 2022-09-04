""" Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""


vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetor3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
resultado = []

for i in range(10):
    resultado.append(vetor1[i])
    resultado.append(vetor2[i])
    resultado.append(vetor3[i])

print(f"3 Lista de vetores intercalados: {resultado}")
