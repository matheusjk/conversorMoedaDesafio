import requests
import pprint
import json

moedas = requests.get('https://economia.awesomeapi.com.br/json/all')
# print(moedas)

# pprint.pprint(moedas.text)

buscar = json.loads(moedas.text)

print(buscar['USD']['high'])