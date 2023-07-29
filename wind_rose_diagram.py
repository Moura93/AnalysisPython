# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:43:17 2023

@author: Felipe Moura
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import pandas as pd
from windrose import WindroseAxes

"""   LEITURA DOS DADOS   """
df = pd.read_excel(r'C:\Users\fmour\Documents\MEGAsync Downloads\Documentos\Mestrado\Python\Base de dados\INMET\tabela (1).xlsx')

"""   PREAPRAÇÃO DOS DADOS   """
dados = df.loc[:,['Data','Hora (UTC)', 'Vel. Vento (m/s)', 'Dir. Vento (m/s)']]
dados['Dir. Vento (rad)'] = dados['Dir. Vento (m/s)']*np.pi/180

theta = dados['Dir. Vento (rad)']
r = dados['Vel. Vento (m/s)']

fig, ax = plt.subplots(figsize=(8,8), dpi=80)
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect('equal')
ax = WindroseAxes.from_ax()
ax.bar(dados['Dir. Vento (m/s)'], r, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
