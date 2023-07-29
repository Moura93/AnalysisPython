# LEITURA DOS DADOS #
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import seaborn as sns

#df = pd.read_excel(r"C:\Users\Felipe\DIAGNOSTICOS.xlsx")
df = pd.read_excel(r"C:\Users\fmour\Documents\MEGAsync Downloads\Documentos\Mestrado\DIAGNOSTICOS.xlsx")

df['Dia'] = pd.to_datetime(df['Registro']).dt.day_name()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)


# GRF 1 - TENSÃO NO PERIODO TOTAL #
fig, ax1 = plt.subplots(figsize=(10,5), label='Tensões')
ax1.plot(df['Registro'], df['Vr [V]'], 'r', label='Fase R')
ax1.plot(df['Registro'], df['Vs [V]'], 'k', label='Fase S')
ax1.plot(df['Registro'], df['Vt [V]'], 'y', label='Fase T')
ax1.axhline(y=233, color='r', linestyle='--', label='Faixa Precária')
ax1.axhline(y=231, color='g', linestyle='--', label='Faixa Adequada')
ax1.axhline(y=202, color='g', linestyle='--')
ax1.axhline(y=191, color='r', linestyle='--')
ax1.set_ylim(0,300)
ax1.grid(True)
ax1.set_title('Tensões')
ax1.legend()
ax1.set_xlabel('Dias')
ax1.set_ylabel('Voltagem')

# GRF 2 - BOXPLOT NO PERIODO TOTAL #
ax2 = sns.catplot(data=df, x="Dia", y='Vr [V]', kind="box")

# GRF 3 - TENSÃO DIÁRIA #
filt = (df['Registro'].dt.day == 2)
sexta = df.loc[filt]
sexta['hora'] = sexta['Registro'].dt.time
sexta['hora'] = sexta['hora'].astype(str)

# g = interpolate.interp1d(sexta['Registro'], sexta['Vr [V]'], kind='nearest')
# ynew = g(sexta['Timestamp'])
fig3, ax3 = plt.subplots(figsize=(10,5), label='Tensão Diária')
ax3.plot(sexta['hora'],sexta['S [VA]']/100, color="green", drawstyle="steps-post")
ax3.tick_params(axis='x', labelrotation = 90)
ax3.set_xlabel('HORA')
ax3.set_ylabel('[MVA]')
ax3.grid(True)

# GRF 4 - HISTOGRAMA TENSÃO #
fig4, ax4 = plt.subplots(figsize=(10,5), label='Histograma Tensão')
ax4.hist(df['Vr [V]'], bins=30, range=(185,245), density=True, histtype='bar', rwidth=0.8)


plt.show()
