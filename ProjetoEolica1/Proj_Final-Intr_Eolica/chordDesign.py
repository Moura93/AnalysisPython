import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import xlsxwriter

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)

vel_angular_rotor = (35 / 60) * 2 * math.pi

Vel_desenho = 10
Numero_Pas = 3

alpha = 4
Cl = 0.7725
Cd = 0.0060

def Calculo_Raio_Rotor(potencia_nominal, coeficiente_potencia, velocidade_nominal, eficiencia_eletrica):
    Densidade_ar = 1.225
    area_transversal = (potencia_nominal * 2 * 1000) / (
            coeficiente_potencia * eficiencia_eletrica * Densidade_ar * velocidade_nominal ** 3)
    R = math.sqrt(area_transversal / math.pi)
    return R

# potencia_nominal = float(input('Insira a potência nominal(kw): '))
# coeficiente_potencia = float(input('Insira o coeficiente nominal: '))
# eficiencia_eletrica = float(input('Insira a eficiência elétrica do aerogerador: '))

potencia_nominal = 400
coeficiente_potencia = 0.3
eficiencia_eletrica = 0.9
velocidade_nominal = 14
# velocidade_nominal = float(input('Insira a velocidade nominal: '))

R = Calculo_Raio_Rotor(potencia_nominal, coeficiente_potencia, velocidade_nominal, eficiencia_eletrica)

print(f'O raio é: {R} metros')

Lamb = vel_angular_rotor * R / Vel_desenho

print(f'A razão da velocidade na ponta da pá em relação a velocidade de desenho é: {Lamb}')

l_a = []
l_al = []
l_r = []
l_rR = []
l_C = []
l_CR = []
l_fi = []  # angulo de fluxo
l_Cn = []
l_Ct = []
l_Solidez = []
beta = 0  # angulo de pith
l_beta = []
l_coef = []
lamb_loc = 0
l_lamb_loc = []

i = 0
k = 0

for r in np.arange(R / 80, R, R / 40):
    flag = 0
    lamb_loc = vel_angular_rotor * r / Vel_desenho
    l_lamb_loc.append(lamb_loc)
    x = lamb_loc
    l_r.append(r)
    l_rR.append(r / R)
    coef = [16, -24, (9 - 3 * x ** 2), (x ** 2 - 1)]
    l_coef.append(np.roots(coef))

    for k in np.roots(coef):
        flag == 0
        while flag != 1:
            if k <= 1 and k > 0:
                l_a.append(k)
                flag += 1
            else:
                break

for z in l_a:
    al = (1 - 3 * z) / (4 * z - 1)
    l_al.append(al)

for r in np.arange(R / 80, R, R / 40):
    fi = np.arctan(((1 - l_a[i]) * velocidade_nominal) / (vel_angular_rotor * r * (1 + l_al[i])))
    l_fi.append(fi)
    beta = np.degrees(fi) - alpha
    #beta= np.radians(beta)
    l_beta.append(beta)
    Cn = Cl * np.cos(fi) + Cd * np.sin(fi)
    l_Cn.append(Cn)
    Ct = Cl * np.sin(fi) - Cd * np.cos(fi)
    l_Ct.append(Ct)
    lamb_loc = vel_angular_rotor * r / Vel_desenho
    C = (8 * math.pi * l_a[i] *r * (np.sin(fi)) ** 2) / ((1 - l_a[i]) * Numero_Pas  * Cn)
    Solidez = C *Numero_Pas/(2 * math.pi * r)
    l_Solidez.append(Solidez)
    l_C.append(C)
    l_CR.append(C / r)
    i += 1

df = pd.DataFrame({'l_a': l_a, 'l_al': l_al, 'l_C': l_C, 'l_Solidez': l_Solidez, 'l_fi': l_fi, 'l_lambda': l_lamb_loc, 'l_beta': l_beta, 'l_r': l_r})

writer = pd.ExcelWriter('dadosConstantes.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='coeficientes')
writer.close()

# print(l_coef)
# print(len(l_coef))
#
# print(l_a)
# print(len(l_a))
#
# print(l_al)
# print(len(l_al))
#
# print(l_C)
# print(len(l_C))
#
# print(l_Solidez)
# print(len(l_Solidez))
#
# print(l_fi)
# print(len(l_fi))
#
# print(l_lamb_loc)
# print(len(l_lamb_loc))
#
# print(l_beta)
# print(len(l_beta))
#
# print(l_r)
# print(len(l_r))

plt.subplot(2, 1, 1)
plt.plot(df['l_r']/R, df['l_C']/R)
plt.xlim([0.1,1])
plt.xlabel('r/R')
plt.ylabel('Corda/R')
plt.title('Corda X R')

plt.subplot(2, 1, 2)
plt.plot(df['l_r']/R, df['l_beta'])
plt.xlim([0.1,1])
plt.xlabel('r/R')
plt.ylabel('Passo (°)')
plt.title('Passo [°] X R [m]')
print(df)
plt.tight_layout(pad=3)
plt.show()
