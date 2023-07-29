# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:07:02 2023

@author: Felipe Moura
@title: Joggofi
"""

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

API_KEY = 'KEWY99JXPYK2WTDVGLBVGTBB3XD5O02N'
ID = '1554347'
SERIAL = '1523684'

START = '2021-01-01 07:00:00'
END = '2022-01-01 20:00:00'

# =============================================================================
# link = f'https://monitoringapi.solaredge.com/site/{ID}/energy?timeUnit=DAY&endDate={END}&startDate={START}&api_key={API_KEY}'
# geracao = pd.DataFrame.from_dict(requisicao_dic['energy']['values'])
# x = np.linspace(1, len(geracao), len(geracao))
# plt.figure(figsize=(20,6))
# plt.plot(x, geracao['value'])
# plt.show()
# =============================================================================

#link = f'https://monitoringapi.solaredge.com/sites/list?size=5&searchText=Lyon&sortProperty=name&sortOrder=ASC&api_key={API_KEY}'
link = f'https://monitoringapi.solaredge.com/site/{ID}/details?api_key={API_KEY}'
#link = f'https://monitoringapi.solaredge.com/site/{ID}/dataPeriod?api_key={API_KEY}'
#link = f'https://monitoringapi.solaredge.com/sites/{ID}/dataPeriod?api_key={API_KEY}'
#link = f'https://monitoringapi.solaredge.com/ site/{ID}/overview?api_key={API_KEY}'
#link = f'https://monitoringapi.solaredge.com/site/{ID}/currentPowerFlow?api_key={API_KEY}'
#link = f'https://monitoringapi.solaredge.com/site/{ID}/storageData.json?startTime={START}&endTime={END}&api_key={API_KEY}'
#link = f' https://monitoringapi.solaredge.com/equipment/{ID}/12345678-90/data?startTime=2013-05-05%2011:00:00&endTime=2013-05-05%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O'

requisicao = requests.get(link)
requisicao_dic = requisicao.json()

print(json.dumps(requisicao_dic, indent=5))
