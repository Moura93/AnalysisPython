# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 23:53:35 2023

@author: fmour
"""
# BIBLIOTECAS #
import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import seaborn as sns

# SOLICITAÇÃO API #
API_KEY = 'KEWY99JXPYK2WTDVGLBVGTBB3XD5O02N'
ID = '1554347'

START2 = '2022-01-01%2000:00:00'
END2 = '2022-01-07%2023:00:00'

inverter_technical_data = f'https://monitoringapi.solaredge.com/equipment/{ID}/7E17B5E7-31/data?startTime={START2}&endTime={END2}&api_key={API_KEY}'
InverterTechnicalData_dic = requests.get(inverter_technical_data).json()

# DADOS DO SISTEMA #
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

tensao = {
    'tempo': TIME,
    'R': VCA_F1,
    'S': VCA_F2,
    'T': VCA_F3,
    }
        
df = pd.DataFrame(data=tensao)     
df['tempo'] = pd.to_datetime(df['tempo'])
df['tempo'] = df['tempo'].dt.strftime('%Y-%m-%d')
df = df.groupby(['tempo'])

g = sns.catplot(data=df, x="tempo", y="R", kind="box").set(title="Variação de Tensão", xlabel='Dia', ylabel='Tensão [V]')
g.set_xticklabels(rotation=90)
plt.show()


