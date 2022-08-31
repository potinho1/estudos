import json

from minha_agenda import MinhaAgenda

arquivo = 'contatos.json'

contatos = []

try:
    with open(arquivo) as f:
        contatos = json.load(f)

except FileNotFoundError:
    pass

agenda = MinhaAgenda(contatos)
agenda.run()


with open(arquivo, 'w') as f:
    json.dump(agenda.contatos_dict, f)
