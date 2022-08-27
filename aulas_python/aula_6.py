'''carros_dict = {'celta': 10000, 'fox': 15000, 'fit': 30000, 'corolla': 60000}
print(carros_dict['celta'])

# Adicionando keys no dicionário
new_dict = {'idade': 21, 'nome': 'potinho', 'profissao': 'dev', }
new_dict['pai'] = 'joao'
print(new_dict)

# Começando com um dicionário vazio
contatos = {}
contatos['potinho'] = 123456
contatos['joao'] = 67890
print(contatos)

# Modificar valores em um dicionário
print(contatos['potinho'])
contatos['potinho'] = 12435687
print(contatos['potinho'])

# Removendo valores de um dicionário
print(contatos)
del contatos['potinho']
print(contatos)


# Várias informações sobre objeto
carro = {'ano': 2021, 'modelo': 'gol', 'preco': 32000, 'motor': 1.6}
print(carro)
print(f"Ano do carro: {carro['ano']}")
print(f"Modelo do carro: {carro['modelo']}")


# Acessando valores de um dicionário com método .get()
carro = {'ano': 2021, 'modelo': 'gol', 'preco': 32000, 'motor': 1.6}
print(carro.get('ano', "Nenhum ano foi informado"))
print(carro.get('cor', "Nenhuma cor foi informada"))

# Loop através dos pares key:value de um dicionário
funcionario = {
    'primerio_nome': 'potinho',
    'segundo_nome': 'gomes',
    'função': 'dev',
    'salário': 5000
}

for key, value in funcionario.items():
    print(f"key: {key}\nvalue: {value}\n")

# Loop através dos pares key:value
contatos = {}
contatos['potinho'] = 123456
contatos['joao'] = 67890

for nome, telefone in contatos.items():
    print(f"O telefone do {nome} é {telefone}")

# Loop através das keys
contatos = {}
contatos['potinho'] = 123456
contatos['joao'] = 67890

for nome in contatos.keys():
    print(f"Olá {nome}! Seu número continua {contatos[nome]}?")

# Loop através dos values
pesquisa_comidas = {
    'joao': 'churrasco',
    'ana': 'pizza',
    'ba': 'japones',
    'laura': 'pao',
    'alisson': 'carne'
}

for comida in set(pesquisa_comidas.values()):  # ele apaga os valores repetidos
    print(comida)

# Criando um set
set_cidades = {"rio de janeiro", "São Paulo", "Belo horizonte", "São Paulo", }

print(set_cidades)

# Aninhamento
# Lista de dicionários

funcionario1 = {
    'primeiro_nome': 'potinho',
    'segundo_nome': 'gomes',
    'função': 'dev',
    'salário': 5000
}

funcionario2 = {
    'primeiro_nome': 'jao',
    'segundo_nome': 'silva',
    'função': 'dev jr',
    'salário': 4000
}

funcionario3 = {
    'primeiro_nome': 'vitor',
    'segundo_nome': 'gomes',
    'função': 'dev pleno',
    'salário': 8000
}

funcionarios = [funcionario1, funcionario2, funcionario3]

for funcionario in funcionarios:
    print(
        f"Nome do funcionário: {funcionario['primeiro_nome']} {funcionario['segundo_nome']}")
    print(f"Função: {funcionario['função']}")
    print(f"Salário: {funcionario['salário']}\n")

# Lista de dicionário
# Cada funcionário recebeu aumento de 20%
# O salárip mínimo na empresa passou a ser R$3.000,00
funcionario1 = {
    'primeiro_nome': 'potinho',
    'segundo_nome': 'gomes',
    'função': 'dev',
    'salário': 5000
}

funcionario2 = {
    'primeiro_nome': 'jao',
    'segundo_nome': 'silva',
    'função': 'dev jr',
    'salário': 4000
}

funcionario3 = {
    'primeiro_nome': 'vitor',
    'segundo_nome': 'gomes',
    'função': 'dev pleno',
    'salário': 8000
}

funcionario4 = {
    'primeiro_nome': 'davi',
    'segundo_nome': 'gomes',
    'função': 'dev pleno',
    'salário': 2000
}

funcionarios = [funcionario1, funcionario2, funcionario3, funcionario4]

for funcionario in funcionarios:
    print(
        f"Nome do funcionário: {funcionario['primeiro_nome']} {funcionario['segundo_nome']}")
    print(f"Salário antigo: {funcionario['salário']}")
    funcionario['salário'] = 1.2 * funcionario['salário']
    if funcionario['salário'] < 3000:
        funcionario['salário'] = 3000
    print(f"Salário ajustado: {funcionario['salário']}\n")


# Aninhando uma lista em um dicionário
pedido = {
    'prato': 'x-tudo',
    'adicionais': ['+1 hambuerguer', 'queijo extra', 'batata frita', 'ovo frito']
}

print(f"Você pediu um {pedido['prato']}")

print("Adicionais:")
for adicional in pedido['adicionais']:
    print(adicional)


cores_favoritas = {
    'potinho': ['azul', 'preto', 'cinza'],
    'joão': ['vermelho', 'preto', 'branco'],
    'ana': ['rosa'],
    'laura': ['roxo']
}

for nome, cores in cores_favoritas.items():
    print(f"As cores do(a) {nome} são: ")
    for cor in cores:
        print(cor)
    print("\n")
'''

# Dicionário dentro de um dicionário

usuarios = {
    'joaozinho': {'nome': 'joao', 'email': 'joaozinho@gmail.com'},
    'ana': {'nome': 'analaurinha', 'email': 'analaura@gmail.com'},
    'laura': {'nome': 'laura', 'email': 'lausantos@gmail.com'},
}

for usuario, usuario_info in usuarios.items():
    print(f"{usuario}: ")
    print(f"Nome: {usuario_info['nome']}")
    print(f"Email: {usuario_info['email']}\n")
