# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:02:44 2023

@author: Felipe Moura
"""

"""   BIBLIOTECAS USADAS   """
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import pandas as pd

""" \/  CONVERSÃO POL 2 RAD  \/
def polar2z(r,theta):
    return r * exp( 1j * theta )

def z2polar(z):
    return ( abs(z), angle(z) )
"""

"""   LEITURA DOS DADOS   """
df = pd.read_excel(r'C:\Users\fmour\Documents\MEGAsync Downloads\Documentos\Mestrado\Python\Base de dados\INMET\tabela (1).xlsx')

"""   PREAPRAÇÃO DOS DADOS   """
dados = df[['Data','Hora (UTC)', 'Vel. Vento (m/s)', 'Dir. Vento (m/s)']]
dados['Dir. Vento (rad)'] = dados['Dir. Vento (m/s)']*np.pi/180

theta = dados['Dir. Vento (rad)']
r = dados['Vel. Vento (m/s)']

"""   INFORMAÇÕES SOBRE A COLUNA DIREÇÃO DO VENTO (EM GRAUS)   """
print(dados['Dir. Vento (m/s)'].describe())

"""   PLOTAGEM DOS GRÁFICOS   """
fig, ax = plt.subplots(dpi=120,subplot_kw=dict(projection='polar'))
plt.style.use('bmh')
c = plt.scatter(theta, r, c=r, s=100*r**2, cmap='hot', lw=0, alpha=0.1)
plt.polar(dados['Dir. Vento (rad)'], dados['Vel. Vento (m/s)'], 'b.', alpha=0.1)
ax.set_title('Velocidade de Direção do Vento')

plt.show()