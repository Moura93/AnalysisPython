# Nesse código é feita:
# 1. junção dos arquivos encontrados
# 2. encontro do módulo da velocidade do vento
# 3. Organização das tabelas
# 4. Interpolação bilinear das velocidades
# 5. Organização final da tabela por ML em colunas


import pandas as pd
import numpy as np
import math
from datetime import datetime, timedelta
import xlsxwriter

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df_paracuru = pd.read_csv(r'PARACURU.csv')

df1 = pd.read_excel(r'dataExcel/Vel_1P_NE_ML_2004-2006.xlsx')
df2 = pd.read_excel(r'dataExcel/Vel_1P_WS_ML_2004-2006.xlsx')
df3 = pd.read_excel(r'dataExcel/Vel_2P_ML_2004-2006.xlsx')

df = pd.concat([df1,df2,df3])

df['datetimes'] = pd.to_datetime(df['datetimes'])

df = df.sort_values(['level','datetimes'], ascending=[True, True])

# ---- : : Módulo da Velocidade : : ----

df['Vel'] = np.sqrt((df['u']**2)+(df['v']**2))

# ---- : : Definição dos Pontos da IBL : : ----

df['Ponto'] = np.where((df['latitude']==-3.25) & (df['longitude']==-38.75), 'P2',
              np.where((df['latitude']==-3.50) & (df['longitude']==-39.00), 'P4',
              np.where((df['latitude']==-3.25) & (df['longitude']==-39.00), 'P1',
              np.where((df['latitude']==-3.50) & (df['longitude']==-38.75), 'P3', 'NP'))))

df=df.drop(["longitude","latitude","u","v"], axis=1)

# ---- : : Divisão de DataFrames por ML : : ----

df128 = df.loc[df['level']==128]
df129 = df.loc[df['level']==129]
df130 = df.loc[df['level']==130]
df131 = df.loc[df['level']==131]
df132 = df.loc[df['level']==132]
df133 = df.loc[df['level']==133]
df134 = df.loc[df['level']==134]
df135 = df.loc[df['level']==135]
df136 = df.loc[df['level']==136]
df137 = df.loc[df['level']==137]

# ---- : : Cálculo do Mod da Vel por IBL: : ----

df128 = df128.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df128['PP'] = (df128['P1']*0.330460 + df128['P2']*0.022428 + df128['P3']*0.041128 + df128['P4']*0.605984)

df129 = df129.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df129['PP'] = (df129['P1']*0.330460 + df129['P2']*0.022428 + df129['P3']*0.041128 + df129['P4']*0.605984)

df130 = df130.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df130['PP'] = (df130['P1']*0.330460 + df130['P2']*0.022428 + df130['P3']*0.041128 + df130['P4']*0.605984)

df131 = df131.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df131['PP'] = (df131['P1']*0.330460 + df131['P2']*0.022428 + df131['P3']*0.041128 + df131['P4']*0.605984)

df132 = df132.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df132['PP'] = (df132['P1']*0.330460 + df132['P2']*0.022428 + df132['P3']*0.041128 + df132['P4']*0.605984)

df133 = df133.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df133['PP'] = (df133['P1']*0.330460 + df133['P2']*0.022428 + df133['P3']*0.041128 + df133['P4']*0.605984)

df134 = df134.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df134['PP'] = (df134['P1']*0.330460 + df134['P2']*0.022428 + df134['P3']*0.041128 + df134['P4']*0.605984)

df135 = df135.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df135['PP'] = (df135['P1']*0.330460 + df135['P2']*0.022428 + df135['P3']*0.041128 + df135['P4']*0.605984)

df136 = df136.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df136['PP'] = (df136['P1']*0.330460 + df136['P2']*0.022428 + df136['P3']*0.041128 + df136['P4']*0.605984)

df137 = df137.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df137['PP'] = (df137['P1']*0.330460 + df137['P2']*0.022428 + df137['P3']*0.041128 + df137['P4']*0.605984)

# ---- : : Organização do Cabeçalho : ----

df128.columns =[s1 + str(s2) for (s1,s2) in df128.columns.tolist()]
df128.reset_index(inplace=True)
df129.columns =[s1 + str(s2) for (s1,s2) in df129.columns.tolist()]
df129.reset_index(inplace=True)
df130.columns =[s1 + str(s2) for (s1,s2) in df130.columns.tolist()]
df130.reset_index(inplace=True)
df131.columns =[s1 + str(s2) for (s1,s2) in df131.columns.tolist()]
df131.reset_index(inplace=True)
df132.columns =[s1 + str(s2) for (s1,s2) in df132.columns.tolist()]
df132.reset_index(inplace=True)
df133.columns =[s1 + str(s2) for (s1,s2) in df133.columns.tolist()]
df133.reset_index(inplace=True)
df134.columns =[s1 + str(s2) for (s1,s2) in df134.columns.tolist()]
df134.reset_index(inplace=True)
df135.columns =[s1 + str(s2) for (s1,s2) in df135.columns.tolist()]
df135.reset_index(inplace=True)
df136.columns =[s1 + str(s2) for (s1,s2) in df136.columns.tolist()]
df136.reset_index(inplace=True)
df137.columns =[s1 + str(s2) for (s1,s2) in df137.columns.tolist()]
df137.reset_index(inplace=True)
df128['level'] = 128
df129['level'] = 129
df130['level'] = 130
df131['level'] = 131
df132['level'] = 132
df133['level'] = 133
df134['level'] = 134
df135['level'] = 135
df136['level'] = 136
df137['level'] = 137

# ---- : : Concatenação das Tabelas : ----

df_pre = pd.concat([df128, df129, df130, df131, df132, df133, df134, df135, df136, df137], ignore_index=True)
df_final = df_pre.loc[:,['datetimes','PP','level']]

# ---- : : Renomeação dos Cabeçalhos : ----

df_final.columns = ['datetimes', 'Vel', 'level']

df_final['datetimes'] = pd.to_datetime(df_final['datetimes'])

# ---- : : Encontro da Hora Local GMT-3 : ----

df_final['datetimes'] = df_final['datetimes']-timedelta(hours=3)

# ---- : : Pivotação da Tabela para se ter os ML em colunas : ----

df_final = df_final.pivot(index='datetimes', columns='level', values='Vel')

writer = pd.ExcelWriter('dataERA5_IBL.xlsx', engine='xlsxwriter')
df_final.to_excel(writer, sheet_name='IBL')
writer.close()