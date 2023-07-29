
import matplotlib.pyplot as plt
import requests
import pandas as pd
import datetime
import json

INICIO = '2023-01-01%2011:00:00'
FIM = '2023-01-02%2011:00:00'
API_KEY = 'C1I0M766MBWOF6OXYK7ZTP9EFGR43D3F'
ID = '1968363'

# link = f'https://monitoringapi.solaredge.com/site/1/powerDetails?meters=PRODUCTION,CONSUMPTION&startTime={INICIO}&endTime={FIM}&api_key={API_KEY}'
link = f'https://monitoringapi.solaredge.com/sites/{ID}/power?startTime={INICIO}&endTime={FIM}&api_key={API_KEY}'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

requisicao = requests.get(link).json()
req_norm = pd.json_normalize(requisicao['powerDateValuesList']['siteEnergyList'])
req_dump = json.dumps(int(requisicao['powerDateValuesList']['siteEnergyList'][0]), indent=3)

print(req_dump)