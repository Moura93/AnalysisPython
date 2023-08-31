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

dif_a = []
dif_al = []
al = a = 0 #FATOR DE INDUÇÃO AXIAL
for r in np.arange(R/80, R, R/40):
    x=(lamb*r)/R
    for a in np.arange(0.01, 1, 0.01):
        for al in np.arange(0.01, 1, 0.01):
            theta = math.atan( ((1-a)*Ud) / ((1+al)*OmegaPq) )
            beta = theta - alpha
            Cn = (Cl*math.cos(math.radians(theta))) + (Cd*math.sin(math.radians(theta)))
            Ct = (Cl*math.sin(math.radians(theta))) - (Cd*math.cos(math.radians(theta)))
            #x = np.sqrt(((16*(a**3)) - (24*(a**2)) + (9*a)-1) / (3*a-1))
            c = (8*math.pi*a*x*(math.sin(math.radians(theta))**2)*R)/((1-a)*B*Cn*lamb)
            sigma = (c*B)/(2*math.pi*B*r)
            a_cal = 1/( ((4*math.sin(math.radians(theta))**2)/(sigma*Cn)) +1)
            al_cal = 1/( ((4*math.sin(math.radians(theta))*math.cos(math.radians(theta)))/(sigma*Ct)) -1)
            a_dif = (a_cal-a)/(a-1)
            al_dif = (al_cal-a)/(al-1)
            dif_a.append(a_dif)
            dif_al.append(al_dif)
            # print("dif a: ", a_dif)
            # print("dif a': ", al_dif)
            # print("Cn: ", Cn)
            # print("Ct: ", Ct)
            # print("Theta: ", theta)
            # print("x: ", Cn)
            # print("c: ", Ct)
            # print("sigma: ", sigma)
            # print("a: ", a)
            # print("a': ", al)
            # print("Cal a: ", a_cal)
            # print("Cal a': ", al_cal)
            # print("")

plt.plot(dif_a, dif_al)
plt.show()