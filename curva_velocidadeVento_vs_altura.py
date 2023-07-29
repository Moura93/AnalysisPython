# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:16:31 2023

@author: Felipe Moura
@title: Curva de Velocidade x Altura
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import pandas as pd
import math as mt

n = 0.1 #coeficiente de rugosidade
# Fator n
#Superficie lisa, lago ou oceano -> 0,1
#Grama baixa -> 0,14
#Vegetação rasteira(até 0,3 m), árvores ocasionais -> 0,16
#Arbustos, árvores ocasionais -> 0,2
#Árvores, construções ocasionais -> 0,22 - 0,24
#Áreas residenciais -> 0,28 - 0,4

Vr = 2.5 #m/s
Hr = 100 #Altura de referência
#Lei da Potência

H = np.linspace(1, 200, 10000)

V = Vr*(H/Hr)**n

#plt.yscale('log')
plt.subplot(1,2,1)
plt.plot(V, H, color='g')
plt.title("Lei da Potência")
plt.xlabel("Velocidade do Vento (m/s)")
plt.ylabel("Altura (m)")
plt.grid(linewidth = 0.5)

#_______________________________________________________
#Lei Logarítima
r = 0.01 #Comprimento de rugosidade
# r (mm)
#Liso, gelo, lama -> 0,01
#Mar aberto e calmo - 0,2
#Mar agitado -> 0,5
#Neve -> 3
#Gramado -> 8
#Pasto acidentado -> 10
#Campo em declive -> 30
#Cultivado -> 50
#Poucas árvores -> 100
#Muitas árvores, poucos edificios, cercas -> 250
#Florestas -> 500
#Subúrbios -> 1500
#Zonas urbanas com edificios altos -> 3000

Vz = ((np.log(H/r))/(np.log(Hr/r)))*Vr

plt.subplot(1,2,2)
plt.plot(Vz, H, color='r')
plt.title("Lei Logatítima")
plt.xlabel("Velocidade do Vento (m/s)")

plt.grid(linewidth = 0.5)
#plt.grid(linewidth = 0.5)

plt.show()
