import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
import xlsxwriter
from datetime import datetime, timedelta

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df_paracuru = pd.read_csv(r'PARACURU.csv')
df_mlr = pd.read_excel(r'modeloMLR.xlsx')

df_ERA5 = pd.read_excel(r'ERA5_1999-2004_ML134.xlsx')

# ---- : : 2datetime : : ----
ml = 134
param = df_mlr['ML%s' % str(ml)]
print(param)
df_paracuru['DataTime'] = pd.to_datetime(df_paracuru['DataTime'])
df_paracuru.rename(columns={'DataTime': 'datetimes'}, inplace=True)

# ---- : : Aplicação do Modelo com a0, a1, a2, a3, a4 : : ----
df_ERA5['Vel_Paracuru'] = (df_ERA5['P-2']*param[2] + df_ERA5['P-4']*param[4] + df_ERA5['P-3']*param[3] + df_ERA5['P-1']*param[1] ) + param[0]

print(df_ERA5)

df_mlr = df_mlr.drop(["Unnamed: 0"], axis=1)
df_ERA5 = df_ERA5.drop(["Unnamed: 0","P-1","P-2","P-3","P-4"], axis=1)

writer = pd.ExcelWriter('SERIE_ESTENDIDA.xlsx', engine='xlsxwriter')
df_ERA5.to_excel(writer, sheet_name='serie')
writer.close()

# Remover valores não finitos
df_clean = df_ERA5[np.isfinite(df_ERA5['Vel_Paracuru'])]

# Definir os limites dos bins e criar o histograma
bin_width = 1  # Comprimento do bin
bin_start = 0.5  # Início do primeiro bin
bins = [bin_start + i * bin_width for i in range(int((df_clean['Vel_Paracuru'].max() - df_clean['Vel_Paracuru'].min()) / bin_width) + 2)]
hist, bin_edges = np.histogram(df_clean['Vel_Paracuru'], bins=bins)

# Parâmetros da distribuição Weibull
shape, loc, scale = weibull_min.fit(df_clean['Vel_Paracuru'], floc=0)

# Calcular a PDF da distribuição Weibull
x = np.linspace(df_clean['Vel_Paracuru'].min(), df_clean['Vel_Paracuru'].max(), 100)
pdf = weibull_min.pdf(x, shape, loc, scale)
cdf = weibull_min.cdf(x, shape, loc, scale)

# Imprimir os parâmetros da Weibull
print('Shape:', shape) # Fator da forma K
print('Location:', loc) # Posição L
print('Scale:', scale) # Fator de escala A ou lambda
#         K      u - L              u - L
# P(u) = --- * (-------)^K-1 * e^-(-------)^K
#         A        A                  A

#AEPd para cada bin
AEP = [0] * len(bins)

#Densidade do AR
Densidade = 1.215 # Densidade na altura do ML 134

cont = 0

def Pd(v):
    return (1/2)*math.pow(v,3)*np.pi*(16.75**2)*Densidade

for bin in bins:
    AEP[cont] = 8760*((weibull_min.cdf(bin+bin_width,shape,loc,scale)) - (weibull_min.cdf(bin,shape,loc,scale))) * ((Pd(bin+bin_width) + Pd(bin))/2)
    cont += 1

#AEP
print("A Produção de Energia Anual é: {} MWh".format((max(AEP)/1000000).round(3)))

#Índice do Bin mais energético
imax = AEP.index(max(AEP))
print("Número do Bin mais Energético = {}".format(imax+1))
print("Bin Mais Energético = {0:.2f} a {1:.2f}".format(bins[imax],bins[imax+bin_width]))

# Obtenha os limites do intervalo do bin associado a 'imax'
limite_inferior = bin_edges[imax]
limite_superior = bin_edges[imax + 1]

# Calcule a velocidade correspondente ao meio do bin 'imax'
VmaxBin = (limite_inferior + limite_superior) / 2

# Imprima a velocidade correspondente ao meio do bin 'imax'
print('Velocidade Mais Energética: {:.2f} m/s'.format(VmaxBin))


# Plotar o histograma
plt.hist(df_clean['Vel_Paracuru'], bins=bins, edgecolor='black', density=True)

# Plotar a curva da PDF da Weibull
plt.plot(x, pdf, 'r-', label='Weibull PDF')

# Configurar os rótulos e títulos
plt.xlabel('Velocidade')
plt.ylabel('Frequência Relativa')
plt.title('Histograma de Velocidade')

# Exibir a legenda
plt.legend()

# Exibir o histograma com a curva da PDF da Weibull
plt.show()