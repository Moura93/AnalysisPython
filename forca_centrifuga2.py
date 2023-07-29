# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 08:06:43 2023

@author: Felipe Moura
@title: Cálculo Força Centrifuga
"""

from datetime import datetime
import requests
import math as mt
#===================OPEN WEATHER MAP API=======================================
API_KEY = '2a37b35ceabf91008003593bb6f72c55'
cidade = 'madagascar' #ESCOLHA DO LOCAL PARA O CÁLCULO (OBS. NOMES EM INGlÊS)

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(link)
requisicao_dic = requisicao.json()

lat = requisicao_dic['coord']['lat']
L = requisicao_dic['coord']['lon']
wind_speed = requisicao_dic['wind']['speed']
wind_deg = requisicao_dic['wind']['deg']
Lo = requisicao_dic['timezone']/3600
HL = datetime.utcnow().hour +Lo +datetime.utcnow().minute/60 #CÁLCULO DA HORA LOCAL
#===================COROREÇÕES E CONDIÇÕES=====================================
if HL > 24:
    HL = HL-24
#CASO A HORA SOLAR ULTRAPASSE 24H, ELE SUBTRAI 24 PARA TER A HROA DO DIA SEGUINTE
if datetime.utcnow().hour+Lo > 24:
    n = datetime.utcnow().timetuple().tm_yday +1
elif datetime.utcnow().hour-Lo <0:
    n = datetime.utcnow().timetuple().tm_yday -1
else:
    n = datetime.utcnow().timetuple().tm_yday
#ADICIONA UM DIA NO CASO DO LOCAL ESCOLHIDO ESTAR ADIANTADO OU SUBTRAI CASO ESTEJA ATRASADO

#===================CÁLCULO DE w===============================================
B = (360/364)*(n-81)
E = 9.87*mt.sin(mt.radians(2*B))-(7.53*mt.cos(mt.radians(B)))-(1.5*mt.sin(mt.radians(B)))
Corhora = (4*(abs(Lo*15) - abs(L))+E)/60
HS = HL + Corhora
w = (HS -12)*15
#===================CÁLCULO DE DA FORÇA CENTRIFUGA DE CORIOLIS=================
f = 2*mt.radians(w)*mt.sin(mt.radians(lat)) 
Fc = f*wind_speed*mt.cos(mt.radians(wind_deg))
#===================PRINT======================================================
print('Local: ', requisicao_dic['name'],
      '\nHora Local: ', HL,
      '\nDia do ano: ', n,'\nB: ', B,
      '\nE: ', E,'\nHora Solar: ', HS,
      '\nNautical Time Zone : ',Lo*15,'\nLongitude: ',L,
      '\nLatitude: ', lat,
      '\nCorhora: ', Corhora,
      '\nÂngulo Horário: ', w,
      '\nVelocidade do Vento: ', wind_speed, '\nÂngulo do Vento: ', wind_deg,
      '\nForça Centrifuga de Coriolis: ', Fc
      )


