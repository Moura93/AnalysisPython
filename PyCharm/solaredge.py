'''
 ::DESCRIÇÃO::
Programa para obtenção dos dados da API
e retornar pela solicitação

 ::AUTOR::
Felipe Moura Wanderley

 ::DATA::
Inicio: 30/06/2023
Ultima Atulização: 30/06/2023
'''

import requests
import json
import math
import numpy as np
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# VARIÁVEIS DA API / DE ENTRADA#
API_KEY = 'KEWY99JXPYK2WTDVGLBVGTBB3XD5O02N'
ID = '1554347'

START = '2021-01-01'
END = '2021-02-01'

START2 = '2022-01-01%2000:00:00'
END2 = '2022-01-01%2023:00:00'

# LINKS DAS APIS #
site_details = f'https://monitoringapi.solaredge.com/site/{ID}/details?api_key={API_KEY}'
SiteDetails_dic = requests.get(site_details).json()
site_energy = f'https://monitoringapi.solaredge.com/site/{ID}/energy?timeUnit=DAY&endDate={END}&startDate={START}&api_key={API_KEY}'
SiteEnergy_dic = requests.get(site_energy).json()
components_list = f'https://monitoringapi.solaredge.com/equipment/{ID}/list?api_key={API_KEY}'
ComponentsList_dic = requests.get(components_list).json()
inverter_technical_data = f'https://monitoringapi.solaredge.com/equipment/{ID}/7E17B5E7-31/data?startTime={START2}&endTime={END2}&api_key={API_KEY}'
InverterTechnicalData_dic = requests.get(inverter_technical_data).json()

# VARIÁVEIS DE RETORNO #
INV_MDE = [] #MODELO DO INVERSOR
SERIAL = [] #NÚMERO DE SERIAL DOS INVERSORES
INV_POT = [] #POTOÊNCIA DO INVERSOR
MOD_MDE = SiteDetails_dic['details']['primaryModule']['modelName'] #MODELO DO MÓDULO FV
MOD_POT = int(SiteDetails_dic['details']['primaryModule']['maximumPower']) #POTÊNCIA DO MÓDILO FV
QNT_ALERTAS = 0 #QUANTIDADE DE ALERTAS
SITE_START = SiteDetails_dic['details']['installationDate']
STATUS = SiteDetails_dic['details']['status']

TIME = [] #TEMPO DA OCORRÊNCIA (5MIN)
DAYS = [] #DIAS SEQUENCIAS
VCA_F1 = [] #TENSÃO DE FASE 1
VCA_F2 = [] #TENSÃO DE FASE 2
VCA_F3 = [] #TENSÃO DE FASE 3
ICA_F1 = [] #CORRENTE DE FASE 1
ICA_F2 = [] #CORRENTE DE FASE 2
ICA_F3 = [] #CORRENTE DE FASE 3
VCC = [] #TENSÃO CONTINUA
PT_CA = [] #ENERGIA GERADA kWh
S1 = [] #POTÊNCIA APARENTE FASE1
S2 = [] #POTÊNCIA APARENTE FASE2
S3 = [] #POTÊNCIA APARENTE FASE3
Q1 = [] #POTÊNCIA REATIVA FASE1
Q2 = [] #POTÊNCIA REATIVA FASE2
Q3 = [] #POTÊNCIA REATIVA FASE3
P1 = [] #POTÊNCIA ATIVA FASE1
P2 = [] #POTÊNCIA ATIVA FASE2
P3 = [] #POTÊNCIA ATIVA FASE3
PT_CC = [] #POTÊNCIA CC
FR_F1 = [] #FREQUÊNCIA DE FASE 1
FR_F2 = [] #FREQUÊNCIA DE FASE 2
FR_F3 = [] #FREQUÊNCIA DE FASE 3
FP1 = [] #FATOR DE POTÊNCIA FASE1
FP2 = [] #FATOR DE POTÊNCIA FASE2
FP3 = [] #FATOR DE POTÊNCIA FASE3

PR = [] #PERFORMACE RATION

for i in range(len(SiteEnergy_dic['energy']['values'])):
    #print(json.dumps(SiteEnergy_dic['energy']['values'][i]['value'], indent=2))
    PT_CA.append(int(SiteEnergy_dic['energy']['values'][i]['value']))
    DAYS.append(SiteEnergy_dic['energy']['values'][i]['date'])

for j in range(len(ComponentsList_dic['reporters']['list'])):
    INV_MDE.append(ComponentsList_dic['reporters']['list'][j]['model'])
    SERIAL.append(ComponentsList_dic['reporters']['list'][j]['serialNumber'])
# print(json.dumps(InverterTechnicalData_dic, indent=3))
# print(f'Inversores: {INV_MDE}\n Números Seriáis: {SERIAL}')

for i in range(len(InverterTechnicalData_dic['data']['telemetries'])):
    if InverterTechnicalData_dic['data']['telemetries'][i]['inverterMode'] == 'MPPT':
        TIME.append((InverterTechnicalData_dic['data']['telemetries'][i]['date']))
        VCA_F1.append(InverterTechnicalData_dic['data']['telemetries'][i]['L1Data']['acVoltage'])
        VCA_F2.append(InverterTechnicalData_dic['data']['telemetries'][i]['L2Data']['acVoltage'])
        VCA_F3.append(InverterTechnicalData_dic['data']['telemetries'][i]['L3Data']['acVoltage'])
        ICA_F1.append(InverterTechnicalData_dic['data']['telemetries'][i]['L1Data']['acCurrent'])
        ICA_F2.append(InverterTechnicalData_dic['data']['telemetries'][i]['L2Data']['acCurrent'])
        ICA_F3.append(InverterTechnicalData_dic['data']['telemetries'][i]['L3Data']['acCurrent'])
        VCC.append(InverterTechnicalData_dic['data']['telemetries'][i]['dcVoltage'])
        S1.append(InverterTechnicalData_dic['data']['telemetries'][i]['L1Data']['apparentPower'])
        S2.append(InverterTechnicalData_dic['data']['telemetries'][i]['L2Data']['apparentPower'])
        S3.append(InverterTechnicalData_dic['data']['telemetries'][i]['L3Data']['apparentPower'])
        Q1.append(InverterTechnicalData_dic['data']['telemetries'][i]['L1Data']['reactivePower'])
        Q2.append(InverterTechnicalData_dic['data']['telemetries'][i]['L2Data']['reactivePower'])
        Q3.append(InverterTechnicalData_dic['data']['telemetries'][i]['L3Data']['reactivePower'])
        P1.append(InverterTechnicalData_dic['data']['telemetries'][i]['L1Data']['activePower'])
        P2.append(InverterTechnicalData_dic['data']['telemetries'][i]['L2Data']['activePower'])
        P3.append(InverterTechnicalData_dic['data']['telemetries'][i]['L3Data']['activePower'])
        PT_CC.append(InverterTechnicalData_dic['data']['telemetries'][i]['totalActivePower'])
        FR_F1.append(InverterTechnicalData_dic['data']['telemetries'][i]['L1Data']['acFrequency'])
        FR_F2.append(InverterTechnicalData_dic['data']['telemetries'][i]['L2Data']['acFrequency'])
        FR_F3.append(InverterTechnicalData_dic['data']['telemetries'][i]['L3Data']['acFrequency'])
        FP1.append(InverterTechnicalData_dic['data']['telemetries'][i]['L1Data']['cosPhi'])
        FP2.append(InverterTechnicalData_dic['data']['telemetries'][i]['L2Data']['cosPhi'])
        FP3.append(InverterTechnicalData_dic['data']['telemetries'][i]['L3Data']['cosPhi'])

# NORMAL DISTRIBUTION #
mean = statistics.mean(PT_CC)
sd = statistics.stdev(PT_CC)
PT_CC.sort()
plt.subplot(1,2,1)
plt.plot(PT_CC, norm.pdf(PT_CC, mean, sd), alpha=0.5)

# HISTOGRAMA #
plt.subplot(1,2,2)
plt.hist(PT_CC, bins=50, edgecolor='black', alpha=0.5)
plt.xlabel('Energia Diária')
plt.ylabel('freq Dias')
plt.show()
