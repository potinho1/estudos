"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def descricao(self):
        descricao_bola = f"Cor da bola: {self.cor}\n" \
            f"Circunferência da bola: {self.circunferencia}\n"\
            f"Material da bola: {self.material}"
        return descricao_bola

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor


bola1 = Bola("Branca", "10", "Capotão")

print(bola1.descricao())

print("Cor anterior")
print(bola1.cor)
bola1.trocar_cor("Azul")
print("Cor atualizada")
print(bola1.cor)

print(bola1.descricao())
