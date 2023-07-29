# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 08:31:44 2023

Cálculo da queda de tensão

@author: Felipe Moura
"""



l = 100;     #Comprimento do cabo em metros
Ib = 35;     #Corrente do circuito
p = 1/56;    #Resistividade do material contudor Cu=1/56 Ohms mm²/m
V1d = 220;   #Tensão monofásico fase-fase
V3f = 380;   #Tensão trifásico fase-fase
dV = 5;      #Queda de tensão máxima admitida em %. 5% ou 7%

# MONOFÁSICO #
Scm = (200*p*l*Ib)/(dV*V);


# TRIFÁSICO #
Sct = (173.2*p*l*Ib)/(dV*V);

print(Sct)
