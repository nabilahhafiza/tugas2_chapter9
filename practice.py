import requests

api_key = '5975242a-e258-47ea-bf9e-9f794c21ce40'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res = requests.get(url)

definitions = res.json()
for definition in definitions:
  print(definition)