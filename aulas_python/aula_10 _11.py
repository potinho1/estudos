"""
FACEBOOK

Fcaebook tem um objeto chamado usuário, todo mundo que entra e se cadastra, se torna um usuário.

todo objeto/usuário tem atributos:
    - Nome
    - Fotos
    - Lista de amigos
    - Telefone
    - Grupos
    - Posts

Todo usuário vai ter uma lista de métodos (conjunto de ações):
    - Adicionar ou remover fotos
    - Adicionar e remover amigos
    - entrar e pode sair de grupos

O objeto usuário tenta copiar uma pessoa real.

Programação orientada a objetos nós estamos falando de olhar e observar objetos do mundo real, como pessoas e fatos, tentar representar tudo isso em forma de código.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------->

GMAIL

Gmail > email

Objeto email também vai ter seus atributos:
    - Remetente
    - Destinatario
    - Assunto
    - Mensagem
    - Data/Hora - tanto de chegada, quando de saída
    - Anexos

Métodos é aquilo que podemos realizar com o objeto do tipo email:
    - Criar novo
    - Enviar

-------------------------------------------------------------------->

            Todo objeto é baseado em uma classe

-------------------------------------------------------------------->

            String, listas, int e etc todos são objetos

-------------------------------------------------------------------->

Uma Classe é uma receita.
    Diz pra gente como um obejto deve ser criado.
    Quais são os atributos/métodos do objeto.
    Como os objetos baseados nela se comportam.
    Como o objeto interage com outros objetos dentro do seu programa.

---------------------------------------------------------------------->

Todo objeto é uma INSTÂNCIA de uma classe(class).

------------------------------------------------->

Método é uma função definida dentro de um classe.

------------------------------------------------->
"""
'''
print(type(50))

print(type(['potinho', 'ana']))



# Criando um classe
# Criando a classe cachorro


class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade


# Criando uma instância de uma calsse
leon = Cachorro("leon", "boxer", 15)

# Acessando atributos de um objeto

print(leon.nome)

# Criando mensagem dos atributos de um objeto
print(
    f"O meu cachorro chama {leon.nome} ele tem {leon.idade} anos, sua raça é {leon.raca}")


# Aterando classes


class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def sentar(self):
        print(f"{self.nome} se sentou")

    def latir(self):
        print("AU")


leon = Cachorro("leon", "boxer", 15)

# Chamando métodos de um objeto

leon.sentar()

for i in range(10):
    leon.latir()

# Fazer referencia a instância Cachorro

bily = Cachorro("Bily", "buldogue", 12)
bruta = Cachorro("Bruta", "chiuaua", 12)
cindy = Cachorro("Cindy", "Dachsund", 10)

print(bily.idade)
print(bruta.nome)

# Criando a classe Email


class Email:
    def __init__(self, assunto, corpo, remet, dest, anexos=[]):
        self.assunto = assunto
        self.corpo = corpo
        self.remet = remet
        self.dest = dest
        self.anexos = anexos
        self.enviado = False

    def add_anexo(self, anexo_str):
        self.anexos.append(anexo_str)
        print(f"{anexo_str} foi adicionado com sucesso á lista de anexos")

    def ver_rascunho(self):
        print(f"De: {self.remet} | Para:{self.dest}\n")
        print(f"Assunto: {self.assunto}\n")
        print(self.corpo)
        print("\nLista de anexos:")
        for anexo in self.anexos:
            print(anexo)

    def enviar_email(self):
        self.enviado = True
        print(
            f"O email {self.assunto}: foi enviado com sucesso para {self.dest}")


meu_email = Email(
    "IMPORTANTE",
    "Preciso que você me ligue urgentemente.",
    "potinho@gmail.com",
    "potinho123@gmail.com"

)

meu_email.ver_rascunho()

meu_email.add_anexo("Foto_1")

meu_email.add_anexo("Foto da multa")

meu_email.ver_rascunho()

meu_email.enviar_email()

print(meu_email.enviado)


# Parte2

# Criando uma calsse para representar produtos de um e-commerce

# Criando a classe produto


class Produto:
    """ Classe para representar produtos de um e-cormmece"""

    def __init__(self, nome, preco, fabricante):
        """ Inicializa os atributos da classe produto"""
        self.nome = nome
        self.preco = preco
        self.fabricante = fabricante

    def descricao(self):
        """ Retorna uma string formatada com a descrição do produto"""
        descricao_produto = f"Nome do produto: {self.nome}\n" \
                            f"Preço do produto: {self.preco}\n" \
                            f"Fabricado por: {self.fabricante}\n"
        return descricao_produto

# Uma vez que a classe é criada, passamos a maior parte do tempo trabalhando com as instâncias dessa classe.

# Instânciando a classe produto | Criando objetos do tipo produto


produto1 = Produto("Celular, branco, 110v", 5000, "Apple")
produto2 = Produto("Mouse", 120, "Logitech")
produto3 = Produto("Kit kat", 5, "Nestlé")

print(produto1.nome)
print(produto1.preco)
print(produto1.fabricante)
print("\n")

print(produto1.descricao())
print("\n")
print(produto2.descricao())
print("\n")
print(produto3.descricao())
print("\n")

# Nem todo atributo precisa ser recebido por um parâmetro


class Produto:
    """ Classe para representar produtos de um e-cormmece"""

    def __init__(self, nome, preco, fabricante):
        """ Inicializa os atributos da classe produto"""
        self.nome = nome
        self.preco = preco
        self.fabricante = fabricante
        self.garantia = 90  # Quantidade de dias de garantia

    def descricao(self):
        """ Retorna uma string formatada com a descrição do produto"""
        descricao_produto = f"Nome do produto: {self.nome}\n" \
                            f"Preço do produto: {self.preco}\n" \
                            f"Fabricado por: {self.fabricante}\n"\
                            f"Garantia do produto: {self.garantia} dias\n"
        return descricao_produto

# Redefinir as instâncias da classe Produto


produto1 = Produto("Celular, branco, 110v", 5000, "Apple")
produto2 = Produto("Mouse", 120, "Logitech")
produto3 = Produto("Kit kat", 5, "Nestlé")

# Verificar a garantia dos produtos
print(produto1.garantia)
print(produto2.garantia)
print(produto3.garantia)
print("\n")

print(produto1.descricao())
print(produto2.descricao())
print(produto3.descricao())


# Inflação | Modificando valores de atributos

# Alterando atributos diretamente
print("Preço anterior: ")
print(produto1.preco)
produto1.preco = 650
print("Preço atualizado:")
print(produto1.preco)

# Criando um método para alterar atributos


class Produto:
    """ Classe para representar produtos de um e-cormmece"""

    def __init__(self, nome, preco, fabricante):
        """ Inicializa os atributos da classe produto"""
        self.nome = nome
        self.preco = preco
        self.fabricante = fabricante
        self.garantia = 90  # Quantidade de dias de garantia

    def descricao(self):
        """ Retorna uma string formatada com a descrição do produto"""
        descricao_produto = f"Nome do produto: {self.nome}\n" \
                            f"Preço do produto: {self.preco}\n" \
                            f"Fabricado por: {self.fabricante}\n"\
                            f"Garantia do produto: {self.garantia} dias\n"
        return descricao_produto

    def alterar_preco(self, novo_preco):
        """Atribui um novo valor para o atributo preco"""
        self.preco = novo_preco


produto1 = Produto("Celular, branco, 110v", 5000, "Apple")
produto2 = Produto("Mouse", 120, "Logitech")
produto3 = Produto("Kit kat", 5, "Nestlé")

# Testando o método criado

print("Preço aterior")
print(produto1.preco)
produto1.alterar_preco(509)
print("Preço atualizado")
print(produto1.preco)

# Atualizar um atributo para calcular um novo
'''


class Produto:
    """ Classe para representar produtos de um e-cormmece"""

    def __init__(self, nome, preco, fabricante):
        """ Inicializa os atributos da classe produto"""
        self.nome = nome
        self.preco = preco
        self.fabricante = fabricante
        self.garantia = 90  # Quantidade de dias de garantia

    def descricao(self):
        """ Retorna uma string formatada com a descrição do produto"""
        descricao_produto = f"Nome do produto: {self.nome}\n" \
                            f"Preço do produto: {self.preco}\n" \
                            f"Fabricado por: {self.fabricante}\n"\
                            f"Garantia do produto: {self.garantia} dias\n"
        return descricao_produto

    def alterar_preco(self, novo_preco):
        """Atribui um novo valor para o atributo preco"""
        self.preco = novo_preco

    def aumentar_preco_porcent(self, porcent):
        """Aumenta o valor do produto"""
        novo_preco = self.preco * (1+porcent/100)
        self.alterar_preco(novo_preco)


'''
# Redefinindo as instâncias da classe Produto
produto1 = Produto("Celular, branco, 110v", 5000, "Apple")
produto2 = Produto("Mouse", 120, "Logitech")
produto3 = Produto("Kit kat", 5, "Nestlé")

# Testando o médoto aumentando_preco_produto
print("Aumentando o preço do produto1 em 10%")
print("Preço anterior:")
print(produto1.preco)
produto1.aumentar_preco_porcent(10)
print("Preço atualizado:")
print(produto1.preco)

print("Aumentando o preço do produto2 em 50%")
print("Preço anterior:")
print(produto2.preco)
produto2.aumentar_preco_porcent(50)
print("Preço atualizado:")
print(produto2.preco)

print("Aumentando o preço do produto3 em 100%")
print("Preço anterior:")
print(produto3.preco)
produto3.aumentar_preco_porcent(100)
print("Preço atualizado:")
print(produto3.preco)


# Herança (Inheritence): Criando uma classe a partir de uma classe já existente

# Criando classe para categorias de produtos

# Criando a classe Monitor, que herda os métodos e atributos da classe Produto


class Monitor(Produto):
    """Representa apenas monitores, um tipo específico de produto"""

    def __init__(self, nome, preco, fabricante):
        """Inicializa os atributos da classe Monitor"""
        super().__init__(nome, preco, fabricante)  # Chamando atributos da classe Pai


# Criando uma instância da classe Monitor
monitor1 = Monitor("Monitor LED HD", 700, "LG")
print(type(monitor1))

# Chamando métodos da classe Produto, através da um objeto do tipo Monitor
print(monitor1.descricao())
print("\n")

print("Preço anterior")
print(monitor1.preco)
monitor1.alterar_preco(900)
print("Preço atualizado")
print(monitor1.preco)


'''
# Criando métodos e atributos da classe Monitor

# Adicionando métodos e atributos da classe Monitor


class Monitor(Produto):
    """Representa apenas monitores, um tipo específico de produto"""

    def __init__(self, nome, preco, fabricante, polegadas):
        """Inicializa os atributos da classe Monitor"""
        super().__init__(nome, preco, fabricante)  # Chamando atributos da classe Pai
        self.polegadas = polegadas

    def descricao(self):
        # Chama o método descricao() da classe Produto
        descricao_sem_polegadas = super().descricao()
        descricao_monitor = descricao_sem_polegadas + \
            f"Polegadas: {self.polegadas}"
        return descricao_monitor


# Criando novos objetos do tipo Monitor
monitor1 = Monitor("Monitor led", 450, "LG", 15)

# Verificando os atributos dos objetos do tipo Monitor
print("Monitor 1: ")
print(monitor1.nome)
print(monitor1.preco)
print(monitor1.fabricante)
print(monitor1.polegadas)

# Executando métodos dos objetos do tipo Monitor
print(monitor1.descricao())


# Objetos como Atributos

# Classe Fabricante

# Criando a classe fabricante
class Fabricante():
    """ Representa o fabricante dos produtos"""

    def __init__(self, nome, cnpj, telefone):
        """ Inicializa os atributos da classe"""
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone

    def descrever_fabricante(self):
        """ Mostra informações do fabricante"""
        print(f"Emepresa: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Tel: {self.telefone}")


# Criando objetos do tipo Fabricante
fabricante_LG = Fabricante("LG", 1234561245, 12321145)
fabricante_Brastemp = Fabricante("Brastemp", 356774554332, 3234457678)

# Armazenando objetos do tipo Fabricante em atributos do pordutos
produto4 = Produto("Geladeira", 3000, fabricante_Brastemp)
produto5 = Produto("Celular", 4500, fabricante_LG)

# Manipulando objetos do tipo Fabricante através dos atributos de produtos
print(produto4.fabricante.nome)
print(produto5.fabricante.nome)
print("\n")
produto4.fabricante.descrever_fabricante()
print("\n")
produto5.fabricante.descrever_fabricante()
