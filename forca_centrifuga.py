# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:14:51 2023

@author: Felipe Moura
@title: Força Centrifuga
"""
import requests
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import pandas as pd
import math as mt

API_KEY = '2a37b35ceabf91008003593bb6f72c55'
cidade = 'recife'

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(link)
requisicao_dic = requisicao.json()

lat = requisicao_dic['coord']['lat']
lon = requisicao_dic['coord']['lon']
wind_speed = requisicao_dic['wind']['speed']
wind_deg = requisicao_dic['wind']['deg']
print("A latitude e longitude de ", cidade, " são:", lat, " e ", lon)

