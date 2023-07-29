import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv(r'naca63-415.csv')

Pn = 400000 #W
freq_angular = 35 #rpm
OmegaPq = (35/60)*2*math.pi
ro = 1.225 #kg/m³
cp = 0.3
nc = 0.9
n = cp*nc
Un = 14 #m/s² Velocidade Nominal
Ud = 9 #m/s² Velocidade de Desenho

A = 2*Pn/(ro*n*(Un**3))
R = np.sqrt(A/math.pi)
df['cl/cd'] = abs(df['Cl'])/abs(df['Cd'])
lamb = OmegaPq*R/Ud

print("Área: ",A)
print("Raio: ",R)
print("OmegaPq: ",R)
print("Lambda: ",lamb)
