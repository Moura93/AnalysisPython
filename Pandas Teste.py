# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:20:32 2023

@author: Felipe Moura
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import pandas as pd
import math as mt

df = pd.read_excel(r'C:\Users\fmour\Downloads\tabela (1).xlsx')

vento = df.loc[:,'Vel. Vento (m/s)'];
"""
print(vento.describe())

#plot
fig, ax = plt.subplots()

ax.hist(vento, bins=100, linewidth=0.1, edgecolor="white")

ax.set(xlim=(0, 10), xticks=np.arange(1, 10))

plt.show()
"""

direcao = df.loc[:,'Dir. Vento (m/s)']

print(direcao.describe())

print(mt.radians(direcao))


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(vento, mt.radians(direcao))
"""
ax.set_rmax(5)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
"""
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()

