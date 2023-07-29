# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 23:20:21 2023

@author: fmour
"""
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import datetime
import seaborn as sns

# =============================================================================
# val_cargaglobalcons: valores de carga global consistidos para utilização nos modelos de previsão
# val_cargaglobal: valores de carga global
# val_cargaglobalsmmgd: valores de carga global líquida de mmgd
# val_cargasupervisionada: parcela da carga atendida por geração supervisionada e intercâmbios, provenientes do sistema de supervisão do ONS
# val_carganaosupervisionada: parcela da carga atendida por geracao não supervisionada, provenientes do sistema de medição de faturamento da CCEE
# val_cargammgd: parcela da carga atendida por micro e mini geração distribuída
# val_consistencia: a parcela de consistências feitas na carga para correção de falhas de medidas e dias atípicos
# =============================================================================

AREA = 'ALPE'
INICIO = '2021-04-01'
FIM = '2021-06-31'

CARGA_VERIFICADA = f'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio={INICIO}&dat_fim={FIM}&cod_areacarga={AREA}'
CARGA_PROGRAMADA = f'https://apicarga.ons.org.br/prd/cargaprogramada?dat_inicio={INICIO}&dat_fim={FIM}&cod_areacarga={AREA}'

#requisicao = requests.get(link)
requisicao = requests.get(CARGA_VERIFICADA)

pd.set_option('display.max_columns', 8)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

requisicao = pd.json_normalize(requisicao.json())
# requisicao['DIA'] = pd.to_datetime(requisicao['dat_referencia'], format='%Y-%m-%d')
# requisicao['DIA'] = requisicao['DIA'].dt.day
requisicao = requisicao.loc[:,['dat_referencia','val_cargaglobal']]
# requisicao_agrupado = requisicao.groupby(['DIA']).mean()

# fig, (ax1, ax2) = plt.subplots(2)

g = sns.catplot(data=requisicao, x="dat_referencia", y="val_cargaglobal", kind="box").set(title="Gráfico de Cargas - Janeiro/2022 - AL+PE", xlabel='Dia', ylabel='Carga [MW]')
g.set_xticklabels(rotation=90)
# requisicao_agrupado.plot()
plt.show()

# cebecario = list(requisicao)
# for i in range(len(cebecario)):
#     print(cebecario[i])