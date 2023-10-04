import math
from sympy import symbols, Eq, solveset, S
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
NACA = pd.read_csv(r'naca63-415.csv')
#Velocidade Nominal
un = 14
ud = 10
#Densidade do Ar
p = 1.225
#Potência Nominal
Pn = 400*1e3
#Rendimento(Mecânico * Elétrico)
Cp = 0.45
ne = 0.95
n = Cp*ne
#Velocidade Angular em rpm
omg = 35
#Conversão para rads/s
omg *= ((2*math.pi)/60)

R = symbols('R')
P = (1/2)*p*math.pi*(R**2)*math.pow(un,3)*n

#Definindo a equação e o parâmetro a ser descoberto
equation = Eq(P, Pn)
#Solução
solutions = solveset(equation, R, domain=S.Reals).args

# Filtrando apenas as soluções positivas
for sol in solutions:
    if sol > 0:
        if sp.im(sol) == 0:
            R = sol

print('Raio do Aerogerador = {0:.2f} m'.format(R))

#Cálculo do λ
lmbda = omg * (R/ud)

print("λ = {0:.2f}".format(lmbda))

lmbda = round(lmbda,0)
if lmbda == 1:
    print('Entre 8-24 Pás')
elif lmbda == 2:
    print('Entre 6-12 Pás')
elif lmbda == 3:
    print('Entre 3-6 Pás')
elif lmbda == 4:
    print('Entre 3-4 Pás')
elif lmbda > 4:
    B = 3
    print('Entre 1-3 Pás')

# Suponhamos que você tenha os dados de NACA definidos antes deste ponto
# NACA = ...

NACA['Cl/Cd'] = abs(NACA["Cl"]/NACA["Cd"])
div = NACA["Cl/Cd"].tolist()
alfa = NACA["alfa"].tolist()
max_div = max(div)
angle = alfa[div.index(max_div)]
#Número de CL e CD
Cl = NACA['Cl'].tolist()
Cd = NACA['Cd'].tolist()
CL = Cl[div.index(max_div)]
CD = Cd[div.index(max_div)]
#Ponto Ótimo
Ponto = (angle,max(div))
print("Ângulo de Ataque Ótimo = {0:.2f}°".format(angle))
df_desenho = pd.DataFrame()

#Número de Seções
N_sec = 40
sec = R/N_sec
for i in range(N_sec):
    if i == 0:
        df_desenho.at[i,'r (seção)'] = sec/2
    else:
        df_desenho.at[i,'r (seção)'] = df_desenho.at[i-1,'r (seção)'] + sec

#Ângulo de fluxo
for i in range(N_sec):
    lbdr = lmbda*(df_desenho.at[i,'r (seção)']/R)
    df_desenho.at[i,'λr'] = lbdr

for i in range(N_sec):
    a = symbols('a')
    x = df_desenho.at[i,'λr']
    fa = 16*(a**3) - 24*(a**2) + a*(9 - 3*(x**2)) - 1 + (x**2)
    equation = Eq(fa, 0)
    solutions = solveset(equation, a, domain=S.Reals).args
    # Filtrando apenas as soluções positivas
    list = []
    for sol in solutions:
        if sp.im(sol) == 0:
            if sol > 0 and sol <= 1:
                list.append(sol)
    if list == []:
        a = max(solutions)
    else:
        a = max(list)
    df_desenho.at[i,'a'] = a

df_desenho["a'"] = (1-3*df_desenho['a'])/(4*df_desenho['a'] - 1)

for i in range(N_sec):
    df_desenho.at[i,'φ (rad/s)'] = abs(math.atan(((1-df_desenho.at[i,"a"])*ud)/((1+df_desenho.at[i,"a'"])*omg*df_desenho.at[i,'r (seção)'])))
    df_desenho.at[i,'Ângulo de fluxo(φ)'] = math.degrees(df_desenho.at[i,'φ (rad/s)'])
    df_desenho.at[i,'β'] = df_desenho.at[i,'Ângulo de fluxo(φ)'] - angle
    df_desenho.at[i,'Cn'] = (math.cos(df_desenho.at[i,'φ (rad/s)']))*CL + (math.sin(df_desenho.at[i,'φ (rad/s)']))*CD
    df_desenho.at[i,'Ct'] = (math.sin(df_desenho.at[i,'φ (rad/s)']))*CL - (math.cos(df_desenho.at[i,'φ (rad/s)']))*CD
    chord = 8*math.pi*(df_desenho.at[i,'r (seção)'])*(df_desenho.at[i,'a'])*math.pow(math.sin(df_desenho.at[i,'φ (rad/s)']),2)
    chord /= ((1-(df_desenho.at[i,'a']))*B*df_desenho.at[i,'Cn'])
    df_desenho.at[i,'Corda(r)'] = chord
    df_desenho.at[i,'Solidez σ'] = ((df_desenho.at[i,'Corda(r)']*B)/(2*math.pi*df_desenho.at[i,'r (seção)']))

# Defina o valor máximo para o eixo x
valor_maximo_x = 1  # Altere este valor conforme necessário

Cl = NACA["Cl"].tolist()
Cd = NACA["Cd"].tolist()

def buscar_valor(valor,list):
    i = 0
    while valor > list[i]:
        i += 1
    imin = i - 1
    imax = i
    return imin,imax

#y = y1 + (x-x1) *((y2-y1)/(x2-x1))
def interpolation(angle):
    imin,imax = buscar_valor(angle,alfa)
    Slope_CL = (Cl[imax] - Cl[imin]) / (alfa[imax] - alfa[imin])
    Slope_CD = (Cd[imax] - Cd[imin]) / (alfa[imax] - alfa[imin])
    CL = Cl[imin] + Slope_CL * (angle - alfa[imin])
    CD = Cd[imin] + Slope_CD * (angle - alfa[imin])
    return CL,CD

#Definir Margem de Erro
Erro = 0.2
N_repetitions = 500
cont = 0
list = []
velocity = {}

for u in range(3,un+1):
    df_Hansen = pd.DataFrame()
    df_Hansen['r (seção)'] = df_desenho['r (seção)']
    df_Hansen['β'] = df_desenho['β']
    df_Hansen['Solidez σ'] = df_desenho['Solidez σ']
    df_Hansen["a (Iteração)"] = 1/3
    df_Hansen["a' (Iteração)"] = 0
    list.append(str(u))

    for i in range(N_sec):
        erro_a = 0.5
        erro_al = 0.5
        phi = 0
        a = 0
        al = 0

        for j in range(N_repetitions):
            phi = ((1 - df_Hansen.at[i,"a (Iteração)"])*u)
            phi /= ((1 + df_Hansen.at[i,"a' (Iteração)"])*omg*df_Hansen.at[i,'r (seção)'])
            phi = abs(phi)
            phi = math.atan(phi)
            df_Hansen.at[i,'φ (rad/s)'] = phi
            df_Hansen.at[i,'Ângulo de fluxo(φ)'] = math.degrees(df_Hansen.at[i,'φ (rad/s)'])
            df_Hansen.at[i,'Ângulo de Ataque(α)'] =  df_Hansen.at[i,'Ângulo de fluxo(φ)'] - df_Hansen.at[i,'β']
            df_Hansen.at[i,'CL'],df_Hansen.at[i,'CD'] = interpolation(df_Hansen.at[i,'Ângulo de Ataque(α)'])
            df_Hansen.at[i,'Cn'] = (math.cos(df_Hansen.at[i,'φ (rad/s)']))*df_Hansen.at[i,'CL'] + (math.sin(df_Hansen.at[i,'φ (rad/s)']))*df_Hansen.at[i,'CD']
            df_Hansen.at[i,'Ct'] = (math.sin(df_Hansen.at[i,'φ (rad/s)']))*df_Hansen.at[i,'CL'] - (math.cos(df_Hansen.at[i,'φ (rad/s)']))*df_Hansen.at[i,'CD']
            if erro_a > Erro:
                a = 4*math.pow(math.sin(df_Hansen.at[i,'φ (rad/s)']),2)
                a /= (df_Hansen.at[i,'Solidez σ']*df_Hansen.at[i,'Cn'])
                a += 1
                a = a**(-1)
                if j > 0:
                    erro_a = (abs(a - df_Hansen.at[i,"a (Iteração)"]))/(df_Hansen.at[i,"a (Iteração)"])
                df_Hansen.at[i,"a (Iteração)"] = a
            else:
                df_Hansen.at[i,"a (Iteração)"] = a
            if erro_al > Erro:
                al = 4*math.sin(df_Hansen.at[i,'φ (rad/s)'])*math.cos(df_Hansen.at[i,'φ (rad/s)'])
                al /= (df_Hansen.at[i,'Solidez σ']*df_Hansen.at[i,'Ct'])
                al -= 1
                al = al**(-1)
                if j > 0:
                    erro_al = (abs(al - df_Hansen.at[i,"a' (Iteração)"]))/(df_Hansen.at[i,"a' (Iteração)"])
                df_Hansen.at[i,"a' (Iteração)"] = al
            else:
                df_Hansen.at[i,"a' (Iteração)"] = al
            if (erro_a < Erro and erro_al < Erro) and j > 0:
                break
        velocity[list[len(list)-1]] = df_Hansen

Power = []
for u in list[2:]:
    df_u = velocity[u]
    list_a = df_u['a (Iteração)'].tolist()
    list_al = df_u["a' (Iteração)"].tolist()
    a_positivos = [valor for valor in list_a if valor > 0 and valor < 1]
    al_positivos = [valor for valor in list_al if valor > 0 and valor < 1]
    dP = 0
    for i in range(N_sec):
        if df_u.at[i,'a (Iteração)'] > 0 and df_u.at[i,'a (Iteração)'] < 1:
            a = df_u.at[i,'a (Iteração)']
        else:
            a = (sum(a_positivos)/len(a_positivos))
        if df_u.at[i,"a' (Iteração)"] > 0 and df_u.at[i,"a' (Iteração)"] < 1:
            al = df_u.at[i,"a' (Iteração)"]
        else:
            al = (sum(al_positivos)/len(al_positivos))
        dP += 4*math.pi*p*((omg)**2)*int(u)*al*(1-a)*((df_u.at[i,'r (seção)'])**3)*sec
    Power.append(dP)

list_upower = []
Power_FULL = []
Pmax = Power[len(Power)-1]
i = 0
for u in range(5,21):
    if u > un:
        Power_FULL.append(Pmax)
    else:
        Power_FULL.append(Power[i])
    list_upower.append((u))
    i += 1

Power_mean = []
list_u = []
for i in range(1,len(Power)):
    Power_mean.append((Power[i] + Power[i-1])*0.5)
    list_u.append((int(list[2:][i]) + int(list[2:][i-1]))*0.5)

Pmax = Power_mean[len(Power_mean)-1]

for u in range(5,21):
    if u > un:
        Power_mean.append(Pmax)
    if u > list_u[len(list_u)-1]:
        list_u.append((u + 0.5))

#Interpolação - Feito em um simulador
Power_mean.append(40475.297785143004)
Power_mean.append(29018.89027720972)
Power_mean = sorted(Power_mean)
list_u.append(3.5)
list_u.append(4.5)
list_u = sorted(list_u)
for i in range(len(list_u)):
    list_u[i] = list_u[i] + 0.5
len(list_u) == len(Power_mean)
# Multiplicação dos dados

# Criar o gráfico
plt.plot(list_u[:-1], np.multiply(Power_mean, (1e-3 * ne)))
plt.xlabel('u (m/s)')
plt.ylabel('Pe (kW)')
plt.title('Curva de Potência')

# Definir os valores do eixo x
plt.xticks([4,6,8,10,12,14,16,18,20])
plt.show()