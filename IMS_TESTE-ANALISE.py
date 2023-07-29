# LEITURA DOS DADOS #
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_excel(r"C:\Users\Felipe\DIAGNOSTICOS.xlsx")

df['Dia'] = df['Registro'].dt.day

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

fig, ax2 = plot.subplot(figsize=(7,5), label='Tensões Diárias')
ax2.plot

plt.show()
