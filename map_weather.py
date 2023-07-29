'''
MAPA DO TEMPO
OPENWEATHER
AUTOR: FELIPE MOURA
'''
import requests

API_KEY = '2a37b35ceabf91008003593bb6f72c55'
Z = 2
X = -8.058641
Y = -34.884859
LAYER = 'precipitation_new'

LINK = f'https://tile.openweathermap.org/map/{LAYER}/{Z}/{X}/{Y}.png?appid={API_KEY}'

requisicao = requests.get(LINK)
print(requisicao.json())
