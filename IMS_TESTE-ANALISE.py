# LEITURA DOS DADOS #
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import seaborn as sns

df = pd.read_excel(r"C:\Users\fmour\Documents\MEGAsync Downloads\Documentos\Mestrado\DIAGNOSTICOS.xlsx")

df['Dia'] = pd.to_datetime(df['Registro']).dt.day_name()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

print(df)

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
sexta['Timestamp'] = pd.to_datetime(sexta['Registro']).values.astype(np.int64)//10*9

g = interpolate.interp1d(sexta['Timestamp'], sexta['Vr [V]'], kind='nearest')
ynew = g(sexta['Timestamp'])
fig2, ax3 = plt.subplots(figsize=(10,5), label='Tensão Diária')
ax3.plot(sexta['Timestamp'],ynew)

plt.show()
