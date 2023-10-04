import pandas as pd
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import math
from windrose import WindroseAxes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# ---- : : Leitura das Tabelas : : ----

df_ml = pd.read_excel(r'dataERA5_IBL.xlsx')
df_paracuru = pd.read_csv(r'PARACURU.csv')

# ---- : : 2datetime : : ----

df_paracuru['DataTime'] = pd.to_datetime(df_paracuru['DataTime'])
df_paracuru.rename(columns={'DataTime': 'datetimes'}, inplace=True)

# ---- : : Merge das Tabelas : : ----

df_merge = df_paracuru.merge(df_ml)
df_merge['datetimes'] = pd.to_datetime(df_merge['datetimes'])

# ---- : : Coeficiente de Pearson : : ----

per_corr = df_merge.loc[:, df_merge.columns!='datetimes'].corr(method='pearson')

writer1 = pd.ExcelWriter('pearson_correlationIBL.xlsx', engine='xlsxwriter')
per_corr.to_excel(writer1, sheet_name='Pearson')
writer1.close()
writer2 = pd.ExcelWriter('paracuruMergeERA5_IBL.xlsx', engine='xlsxwriter')
df_merge.to_excel(writer2, sheet_name='velocidades')
writer2.close()

print("Data Frame Merged:")
print(df_merge)
print("Pearson: ")
print(per_corr)

# ---- : : Definição de Treino e Teste : : ----

y = df_merge['Vel (Mod)']
X = df_merge[[128,129,130,131,132,133,134,135,136,137]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_previsto = modelo.predict(X_test)

print("Coeficiênte de Determinação")
print("R² = {}".format(modelo.score(X_train, y_train).round(4)))
print("")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y_test, y_previsto).round(4))

