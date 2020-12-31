import requests
import pprint

r = requests.get('https://chart.stock-ai.com/history?symbol=%5ETWII&resolution=D&from=1568953895&to=1569891599')

data = r.json()

zipped = zip(data['t'], data['o'], data['h'], data['l'], data['o'], data['v'])
pprint.pprint(list(zipped))