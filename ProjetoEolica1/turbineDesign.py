import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv(r'naca63-415.csv')

Pn = 400000 #W
freq_angular = 35 #rpm
ro = 1.225 #kg/m³
cp = 0.3
nc = 0.9
n = cp*nc
Un = 14 #m/s² Velocidade Nominal
Ud = 9 #m/s² Velocidade de Desenho
B = 3 #Número de pás

OmegaPq = (35/60)*2*math.pi
A = 2*Pn/(ro*n*(Un**3))
R = np.sqrt(A/math.pi)
df['cl/cd'] = abs(df['Cl'])/abs(df['Cd'])
lamb = OmegaPq*R/Ud

alpha = df['alfa'][df['cl/cd'].idxmax()]
Cl = df['Cl'][df['cl/cd'].idxmax()]
Cd = df['Cd'][df['cl/cd'].idxmax()]
for i in range(len(df)):
    if df.loc[i,'alfa']<0:
        df.loc[i,'alfar'] = math.radians(df.loc[i, 'alfa']+360)
    else:
        df.loc[i,'alfar'] = math.radians(df.loc[i, 'alfa'])

print("Área: ",A)
print("Raio: ",R)
print("OmegaPq: ",R)
print("Lambda: ",lamb)
print("alfa max:", alpha)
print(df)

# (1) Initialize a and a', typically a = a' = 0
# (2) Compute the flow angle theta using equation (6.7)
# (3) Compute tht local angle of attack using equation (6.6)
# (4) Read off Cl(alpha) and Cd(alpha) from table
# (5) Compute Cn and Ct from equations (6.12) and (6.13)
# (6) Calculate a and a' from equations (6.23) and (6.24)
# (7) If a and a' has changed more than a certain tolerance, go to step (2) or else finish
# (8) Compute the local loads on the segment of the blades


# while flag < 1:
#     l_cr = []
#     l_rR = []
#     l_Cn = []
#     l_Ct = []
#     l_c = []
#     l_fi = []
#
#     dif_a = []
#     dif_al = []
#
#     l_a = []
#     l_al = []
#     l_acal = []
#     l_alcal = []
#     print("a: ", a_dif)
#     print("a': ", al_dif)
#     for r in np.arange(R / 80, R - (R / 80), R / 40):
#         fi = math.atan(((1 - a) * Ud) / ((1 + al) * OmegaPq * r))
#         beta = fi - alpha
#         Cn = (Cl * math.cos(math.radians(fi))) + (Cd * math.sin(math.radians(fi)))
#         Ct = (Cl * math.sin(math.radians(fi))) - (Cd * math.cos(math.radians(fi)))
#         l_Cn.append(Cn)
#         l_fi.append(fi)
#         l_Ct.append(Ct)
#         l_a.append(a)
#         l_al.append(al)
#         c = (8*math.pi*a*r*(math.sin(math.radians(fi))**2)*R)/((1-a)*B*Cn*lamb)
#         sigma = (c*B)/(2*math.pi*B*r)
#         l_c.append(c)
#         l_cr.append(c/R)
#         l_rR.append(r/R)
#         #CÁLCULO DO a E a'
#         a_cal = 1/( ((4*math.sin(math.radians(fi))**2)/(sigma*Cn)) +1)
#         al_cal = 1/( ((4*math.sin(math.radians(fi))*math.cos(math.radians(fi)))/(sigma*Ct)) -1)
#         #ENCONTRO DO ERRO DO a E a'
#         a_dif = (a_cal-a)/(a-1)
#         al_dif = (al_cal-a)/(al-1)
#         dif_a.append(a_dif)
#         dif_al.append(al_dif)
#         l_acal.append(a_cal)
#         l_alcal.append(al_cal)
#         a = a + 0.01
#         al = al + 0.01
#         if abs(a_dif)>0.1 and abs(al_dif)>0.1:
#             flag = 1
#
# plt.subplot(2,1,1)
# plt.plot(l_rR,l_cr)
# plt.xlabel("r/R")
# plt.ylabel("c/R")
# plt.subplot(2,1,2)
# plt.plot(df['alfa'],df['cl/cd'], 'red')
# plt.xlabel("α")
# plt.ylabel("Cl/Cd")
# plt.show()

l_cr = []
l_rR = []
l_Cn = []
l_Ct = []
l_c = []
l_fi = []
dif_a = []
dif_al = []
l_a = []
l_al = []
l_acal = []
l_alcal = []
for r in np.arange(R / 80, R - (R / 80), R / 40):
    a = 0.001
    al = 0
    a_dif = 0
    al_dif = 0
    flag = 0
    while flag < 1:
        print("a: ", a_dif)
        print("a': ", al_dif)
        fi = math.atan(((1 - a) * Ud) / ((1 + al) * OmegaPq * r))
        beta = fi - alpha
        Cn = (Cl * math.cos(math.radians(fi))) + (Cd * math.sin(math.radians(fi)))
        Ct = (Cl * math.sin(math.radians(fi))) - (Cd * math.cos(math.radians(fi)))
        c = (8*math.pi*a*r*(math.sin(math.radians(fi))**2)*R)/((1-a)*B*Cn*lamb)
        sigma = (c*B)/(2*math.pi*B*r)
        #CÁLCULO DO a E a'
        a_cal = 1/( ((4*math.sin(math.radians(fi))**2)/(sigma*Cn)) +1)
        al_cal = 1/( ((4*math.sin(math.radians(fi))*math.cos(math.radians(fi)))/(sigma*Ct)) -1)
        #ENCONTRO DO ERRO DO a E a'
        a_dif = (a_cal-a)/(a-1)
        al_dif = (al_cal-a)/(al-1)
        a = a + 0.001
        al = al + 0.001
        if abs(a_dif)>0.01 and abs(al_dif)>0.01:
            l_Cn.append(Cn)
            l_fi.append(fi)
            l_Ct.append(Ct)
            l_a.append(a)
            l_al.append(al)
            l_c.append(c)
            l_cr.append(c / R)
            l_rR.append(r / R)
            dif_a.append(a_dif)
            dif_al.append(al_dif)
            l_acal.append(a_cal)
            l_alcal.append(al_cal)
            flag = 1

plt.subplot(2,1,1)
plt.plot(l_rR,l_cr)
plt.title("dif a e a' = 0.01")
plt.xlabel("r/R")
plt.ylabel("c/R")
plt.subplot(2,1,2)
plt.plot(df['alfa'],df['cl/cd'], 'red')
plt.xlabel("α")
plt.ylabel("Cl/Cd")
plt.show()

# VARIABLES
# Cl           -> Lift Coefficient
# Cd           -> Drag Coefficient
# Cn           ->
# Ct           -> Thrust Coefficient
# lamb         ->
# alpha        ->
# OmegaPq      ->
# sigma        ->
# Pn           -> Nominal Power
# freq_angular ->
# ro           -> Air Density
# cp           ->
# nc           ->
# n            ->
# Un           -> Nominal Wind Speed
# Ud           -> Design Wind Speed
# B            -> Number of Blades
# r            ->
# R            -> Radius
# c            -> Length of Chord
# a            ->
# al           ->
# a_dif        ->
# al_dig       ->
# a_cal        ->
# al_cal       ->
# fi           ->