import json

arquivo = 'lista.json'

lista = [1, 2, 3, 4, 5]

with open(arquivo, 'w') as file_obj:
    json.dump(lista, file_obj)
