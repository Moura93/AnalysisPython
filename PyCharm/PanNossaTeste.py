import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r'AREA05.xlsx')

# GRF 1 - POTÊNCIA APARENTE TRIFÁSICA #
fig1, ax1 = plt.subplots(figsize=(10,5), label='Tensões')
ax1.plot(df['Registro'], df['S [VA]'], 'r', label='Potência Aparente Trifásica')
ax1.grid(True)
ax1.set_title('Potência Aparente')
ax1.legend()
ax1.set_xlabel('Dias')
ax1.set_ylabel('S [VA]')

# GRF 2 - TENSÃO NO PERIODO TOTAL #
fig2, ax2 = plt.subplots(figsize=(10,5), label='Tensões')
ax2.plot(df['Registro'], df['Van [V]'], 'r', label='Fase R')
ax2.plot(df['Registro'], df['Vbn [V]'], 'k', label='Fase S')
ax2.plot(df['Registro'], df['Vcn [V]'], 'y', label='Fase T')
ax2.axhline(y=233, color='r', linestyle='--', label='Faixa Precária')
ax2.axhline(y=231, color='g', linestyle='--', label='Faixa Adequada')
ax2.axhline(y=202, color='g', linestyle='--')
ax2.axhline(y=191, color='r', linestyle='--')
ax2.set_ylim(0,300)
ax2.grid(True)
ax2.set_title('Tensões')
ax2.legend()
ax2.set_xlabel('Dias')
ax2.set_ylabel('Voltagem')

plt.show()

print(df)
