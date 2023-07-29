# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:42:44 2023

@author: fmour
"""

import requests
import json

API_KEY = '2a37b35ceabf91008003593bb6f72c55'
cidade = 'ibimirim'

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'
#   link = f'https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt_br'


#requisicao = requests.get(link)
requisicao = requests.get(link)

#requisicao_dic = requisicao.json()

#descricao = requisicao_dic['weather'][0]['description']
#temperatura = requisicao_dic['main']['temp'] - 273.15
#nome = requisicao_dic['name']
#print(descricao, temperatura)
#print(nome)
print(json.dumps(requisicao.json(),indent=3))