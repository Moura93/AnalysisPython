import pandas as pd
import numpy as np
import xlsxwriter
from datetime import datetime, timedelta

df1 = pd.read_excel(r'dataExcel/Vel_1P_NE_ML_1996-1999.xlsx')
df2 = pd.read_excel(r'dataExcel/Vel_1P_WS_ML_1996-1999.xlsx')
df3 = pd.read_excel(r'dataExcel/Vel_2P_ML_1996-1999.xlsx')
df4 = pd.read_excel(r'dataExcel/Vel_1P_NE_ML_2000-2004.xlsx')
df5 = pd.read_excel(r'dataExcel/Vel_1P_WS_ML_2000-2004.xlsx')
df6 = pd.read_excel(r'dataExcel/Vel_2P_ML_2000-2004.xlsx')
df7 = pd.read_excel(r'dataExcel/Vel_1P_NE_ML_2004-2006.xlsx')
df8 = pd.read_excel(r'dataExcel/Vel_1P_WS_ML_2004-2006.xlsx')
df9 = pd.read_excel(r'dataExcel/Vel_2P_ML_2004-2006.xlsx')

# ---- : : 2datetime : : ----

df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9])
df['datetimes'] = pd.to_datetime(df['datetimes'])
df = df.sort_values(['level','datetimes'], ascending=[True, True])

# ---- : : Seleção do Model Level : : ----
df = df.loc[df['level']==134]

# ---- : : Módulo da Velocidade : : ----
df['Vel'] = np.sqrt((df['u']**2)+(df['v']**2))

# ---- : : Nomeação dos Pontos : : ----
df['Ponto'] = np.where((df['latitude']==-3.25) & (df['longitude']==-38.75), 'P2',
              np.where((df['latitude']==-3.50) & (df['longitude']==-39.00), 'P4',
              np.where((df['latitude']==-3.25) & (df['longitude']==-39.00), 'P1',
              np.where((df['latitude']==-3.50) & (df['longitude']==-38.75), 'P3', 'NP'))))

df=df.drop(["longitude","latitude","u","v","level","Unnamed: 0"], axis=1)

# ---- : : Correção da Hora Local : : ----
df['datetimes'] = df['datetimes']-timedelta(hours=3)

df = df.pivot(index='datetimes', columns=['Ponto'], values='Vel')

df.columns =[s1 + '-' + str(s2) for (s1,s2) in df.columns.tolist()]
df.reset_index(inplace=True)

writer = pd.ExcelWriter('ERA5_1999-2004_ML134.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='ML134')
writer.close()
print(df)

