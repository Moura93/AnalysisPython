import pandas as pd
import numpy as np
import math
import xlsxwriter
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df1 = pd.read_excel(r'dataExcel/Vel_1P_NE_ML_2004-2006.xlsx')
df2 = pd.read_excel(r'dataExcel/Vel_1P_WS_ML_2004-2006.xlsx')
df3 = pd.read_excel(r'dataExcel/Vel_2P_ML_2004-2006.xlsx')

df_paracuru = pd.read_csv(r'PARACURU.csv')

# ---- : : 2datetime : : ----

df_paracuru['DataTime'] = pd.to_datetime(df_paracuru['DataTime'])
df_paracuru.rename(columns={'DataTime': 'datetimes'}, inplace=True)

df = pd.concat([df1,df2,df3])

df['datetimes'] = pd.to_datetime(df['datetimes'])

df = df.sort_values(['level','datetimes'], ascending=[True, True])

df['Vel'] = np.sqrt((df['u']**2)+(df['v']**2))

df['Ponto'] = np.where((df['latitude']==-3.25) & (df['longitude']==-38.75), 'P2',
              np.where((df['latitude']==-3.50) & (df['longitude']==-39.00), 'P4',
              np.where((df['latitude']==-3.25) & (df['longitude']==-39.00), 'P1',
              np.where((df['latitude']==-3.50) & (df['longitude']==-38.75), 'P3', 'NP'))))

df=df.drop(["longitude","latitude","u","v"], axis=1)

# ---- : : Correção da Hora Local : : ----
df['datetimes'] = df['datetimes']-timedelta(hours=3)

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

df128 = df128.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df129 = df129.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df130 = df130.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df131 = df131.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df132 = df132.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df133 = df133.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df134 = df134.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df135 = df135.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df136 = df136.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')
df137 = df137.pivot(index='datetimes', columns=['Ponto','level'], values='Vel')

df128.columns =[s1 + '-' + str(s2) for (s1,s2) in df128.columns.tolist()]
df128.reset_index(inplace=True)
df129.columns =[s1 + '-' + str(s2) for (s1,s2) in df129.columns.tolist()]
df129.reset_index(inplace=True)
df130.columns =[s1 + '-' + str(s2) for (s1,s2) in df130.columns.tolist()]
df130.reset_index(inplace=True)
df131.columns =[s1 + '-' + str(s2) for (s1,s2) in df131.columns.tolist()]
df131.reset_index(inplace=True)
df132.columns =[s1 + '-' + str(s2) for (s1,s2) in df132.columns.tolist()]
df132.reset_index(inplace=True)
df133.columns =[s1 + '-' + str(s2) for (s1,s2) in df133.columns.tolist()]
df133.reset_index(inplace=True)
df134.columns =[s1 + '-' + str(s2) for (s1,s2) in df134.columns.tolist()]
df134.reset_index(inplace=True)
df135.columns =[s1 + '-' + str(s2) for (s1,s2) in df135.columns.tolist()]
df135.reset_index(inplace=True)
df136.columns =[s1 + '-' + str(s2) for (s1,s2) in df136.columns.tolist()]
df136.reset_index(inplace=True)
df137.columns =[s1 + '-' + str(s2) for (s1,s2) in df137.columns.tolist()]
df137.reset_index(inplace=True)

df_merge = df_paracuru.merge(df128)
df_merge = df_merge.merge(df129)
df_merge = df_merge.merge(df130)
df_merge = df_merge.merge(df131)
df_merge = df_merge.merge(df132)
df_merge = df_merge.merge(df133)
df_merge = df_merge.merge(df134)
df_merge = df_merge.merge(df135)
df_merge = df_merge.merge(df136)
df_merge = df_merge.merge(df137)
print(df_merge)

# ---- : : Versão 0.1 pela divisão do dataframe manualmente : : ----

half_index = int(len(df_merge)/2)

df_train = df_merge.iloc[:half_index,:]
df_predict = df_merge.iloc[half_index:,:]

print(df_train)
print(df_predict)
# -- ML 128 --
modelo128 = LinearRegression()
X128_train = df_train[['P2-128','P1-128','P3-128','P4-128']]
y128_train = df_train['Vel (Mod)']
modelo128.fit(X128_train, y128_train)
x128_predict = df_predict[['P2-128','P1-128','P3-128','P4-128']]
y128_test = df_predict['Vel (Mod)']

y128_previsto = modelo128.predict(x128_predict)
df_predict['Pred-128'] = y128_previsto

# -- ML 129 --
modelo129 = LinearRegression()
X129_train = df_train[['P2-129','P1-129','P3-129','P4-129']]
y129_train = df_train['Vel (Mod)']
modelo129.fit(X129_train, y129_train)
x129_predict = df_predict[['P2-129','P1-129','P3-129','P4-129']]
y129_test = df_predict['Vel (Mod)']

y129_previsto = modelo129.predict(x129_predict)
df_predict['Pred-129'] = y129_previsto

# -- ML 130 --
modelo130 = LinearRegression()
X130_train = df_train[['P2-130','P1-130','P3-130','P4-130']]
y130_train = df_train['Vel (Mod)']
modelo130.fit(X130_train, y130_train)
x130_predict = df_predict[['P2-130','P1-130','P3-130','P4-130']]
y130_test = df_predict['Vel (Mod)']

y130_previsto = modelo130.predict(x130_predict)
df_predict['Pred-130'] = y130_previsto

# -- ML 131 --
modelo131 = LinearRegression()
X131_train = df_train[['P2-131','P1-131','P3-131','P4-131']]
y131_train = df_train['Vel (Mod)']
modelo131.fit(X131_train, y131_train)
x131_predict = df_predict[['P2-131','P1-131','P3-131','P4-131']]
y131_test = df_predict['Vel (Mod)']

y131_previsto = modelo131.predict(x131_predict)
df_predict['Pred-131'] = y131_previsto

# -- ML 132 --
modelo132 = LinearRegression()
X132_train = df_train[['P2-132','P1-132','P3-132','P4-132']]
y132_train = df_train['Vel (Mod)']
modelo132.fit(X132_train, y132_train)
x132_predict = df_predict[['P2-132','P1-132','P3-132','P4-132']]
y132_test = df_predict['Vel (Mod)']

y132_previsto = modelo132.predict(x132_predict)
df_predict['Pred-132'] = y132_previsto

# -- ML 133 --
modelo133 = LinearRegression()
X133_train = df_train[['P2-133','P1-133','P3-133','P4-133']]
y133_train = df_train['Vel (Mod)']
modelo133.fit(X133_train, y133_train)
x133_predict = df_predict[['P2-133','P1-133','P3-133','P4-133']]
y133_test = df_predict['Vel (Mod)']

y133_previsto = modelo133.predict(x133_predict)
df_predict['Pred-133'] = y133_previsto

# -- ML 134 --
modelo134 = LinearRegression()
X134_train = df_train[['P2-134','P1-134','P3-134','P4-134']]
y134_train = df_train['Vel (Mod)']
modelo134.fit(X134_train, y134_train)
x134_predict = df_predict[['P2-134','P1-134','P3-134','P4-134']]
y134_test = df_predict['Vel (Mod)']

y134_previsto = modelo134.predict(x134_predict)
df_predict['Pred-134'] = y134_previsto

# -- ML 135 --
modelo135 = LinearRegression()
X135_train = df_train[['P2-135','P1-135','P3-135','P4-135']]
y135_train = df_train['Vel (Mod)']
modelo135.fit(X135_train, y135_train)
x135_predict = df_predict[['P2-135','P1-135','P3-135','P4-135']]
y135_test = df_predict['Vel (Mod)']

y135_previsto = modelo135.predict(x135_predict)
df_predict['Pred-135'] = y135_previsto

# -- ML 136 --
modelo136 = LinearRegression()
X136_train = df_train[['P2-136','P1-136','P3-136','P4-136']]
y136_train = df_train['Vel (Mod)']
modelo136.fit(X136_train, y136_train)
x136_predict = df_predict[['P2-136','P1-136','P3-136','P4-136']]
y136_test = df_predict['Vel (Mod)']

y136_previsto = modelo136.predict(x136_predict)
df_predict['Pred-136'] = y136_previsto

# -- ML 137 --
modelo137 = LinearRegression()
X137_train = df_train[['P2-137','P1-137','P3-137','P4-137']]
y137_train = df_train['Vel (Mod)']
modelo137.fit(X137_train, y132_train)
x137_predict = df_predict[['P2-137','P1-137','P3-137','P4-137']]
y137_test = df_predict['Vel (Mod)']

y137_previsto = modelo137.predict(x137_predict)
df_predict['Pred-137'] = y137_previsto


print("ML 128 (287,52m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y128_test, y128_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y128_test, y128_previsto)).round(5)))
print("Multiplicadores: ", modelo128.coef_)
print("Inter: ", modelo128.intercept_)
print("MSE: ", mean_squared_error(y128_test, y128_previsto))
print("EMN: ", abs(y128_test.sum()-y128_previsto.sum())/len(y128_previsto))
print("")
print("ML 129 (244,68m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y129_test, y129_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y129_test, y129_previsto)).round(5)))
print("Multiplicadores: ", modelo129.coef_)
print("Inter: ", modelo129.intercept_)
print("MSE: ", mean_squared_error(y129_test, y129_previsto))
print("EMN: ", abs(y129_test.sum()-y129_previsto.sum())/len(y129_previsto))
print("")
print("ML 130 (205,44m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y130_test, y130_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y130_test, y130_previsto)).round(5)))
print("Multiplicadores: ", modelo130.coef_)
print("Inter: ", modelo130.intercept_)
print("MSE: ", mean_squared_error(y130_test, y130_previsto))
print("EMN: ", abs(y130_test.sum()-y130_previsto.sum())/len(y130_previsto))
print("")
print("ML 131 (169,51m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y131_test, y131_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y131_test, y131_previsto)).round(5)))
print("Multiplicadores: ", modelo131.coef_)
print("Inter: ", modelo131.intercept_)
print("MSE: ", mean_squared_error(y131_test, y131_previsto))
print("EMN: ", abs(y131_test.sum()-y131_previsto.sum())/len(y131_previsto))
print("")
print("ML 132 (136,62m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y132_test, y132_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y132_test, y132_previsto)).round(5)))
print("Multiplicadores: ", modelo132.coef_)
print("Inter: ", modelo132.intercept_)
print("MSE: ", mean_squared_error(y132_test, y132_previsto))
print("EMN: ", abs(y132_test.sum()-y132_previsto.sum())/len(y132_previsto))
print("")
print("ML 133 (106,54m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y133_test, y133_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y133_test, y133_previsto)).round(5)))
print("Multiplicadores: ", modelo133.coef_)
print("Inter: ", modelo133.intercept_)
print("MSE: ", mean_squared_error(y133_test, y133_previsto))
print("EMN: ", abs(y133_test.sum()-y133_previsto.sum())/len(y133_previsto))
print("")
print("ML 134 (79,04m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y134_test, y134_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y134_test, y134_previsto)).round(5)))
print("Multiplicadores: ", modelo134.coef_)
print("Inter: ", modelo134.intercept_)
print("MSE: ", mean_squared_error(y134_test, y134_previsto))
print("EMN: ", abs(y134_test.sum()-y134_previsto.sum())/len(y134_previsto))
print("")
print("ML 135 (53,92m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y135_test, y135_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y135_test, y135_previsto)).round(5)))
print("Multiplicadores: ", modelo135.coef_)
print("Inter: ", modelo135.intercept_)
print("MSE: ", mean_squared_error(y135_test, y135_previsto))
print("EMN: ", abs(y135_test.sum()-y135_previsto.sum())/len(y135_previsto))
print("")
print("ML 136 (30,96m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y136_test, y136_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y136_test, y136_previsto)).round(5)))
print("Multiplicadores: ", modelo136.coef_)
print("Inter: ", modelo136.intercept_)
print("MSE: ", mean_squared_error(y136_test, y136_previsto))
print("EMN: ", abs(y136_test.sum()-y136_previsto.sum())/len(y136_previsto))
print("")
print("ML 137 (10m)")
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y137_test, y137_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y137_test, y137_previsto)).round(5)))
print("Multiplicadores: ", modelo137.coef_)
print("Inter: ", modelo137.intercept_)
print("MSE: ", mean_squared_error(y137_test, y137_previsto))
print("EMN: ", abs(y137_test.sum()-y137_previsto.sum())/len(y137_previsto))

modeloMLR = pd.DataFrame({'ML137': [modelo137.intercept_, modelo137.coef_[1], modelo137.coef_[0], modelo137.coef_[2], modelo137.coef_[3]],
                         'ML136': [modelo136.intercept_, modelo136.coef_[1], modelo136.coef_[0], modelo136.coef_[2], modelo136.coef_[3]],
                         'ML135': [modelo135.intercept_, modelo135.coef_[1], modelo135.coef_[0], modelo135.coef_[2], modelo135.coef_[3]],
                         'ML134': [modelo134.intercept_, modelo134.coef_[1], modelo134.coef_[0], modelo134.coef_[2], modelo134.coef_[3]],
                         'ML133': [modelo133.intercept_, modelo133.coef_[1], modelo133.coef_[0], modelo133.coef_[2], modelo133.coef_[3]],
                         'ML132': [modelo132.intercept_, modelo132.coef_[1], modelo132.coef_[0], modelo132.coef_[2], modelo132.coef_[3]],
                         'ML131': [modelo131.intercept_, modelo131.coef_[1], modelo131.coef_[0], modelo131.coef_[2], modelo131.coef_[3]],
                         'ML130': [modelo130.intercept_, modelo130.coef_[1], modelo130.coef_[0], modelo130.coef_[2], modelo130.coef_[3]],
                         'ML129': [modelo129.intercept_, modelo129.coef_[1], modelo129.coef_[0], modelo129.coef_[2], modelo129.coef_[3]],
                         'ML128': [modelo128.intercept_, modelo128.coef_[1], modelo128.coef_[0], modelo128.coef_[2], modelo128.coef_[3]]})

print(modeloMLR)
writer = pd.ExcelWriter('modeloMLR.xlsx', engine='xlsxwriter')
modeloMLR.to_excel(writer, sheet_name='MLR')
writer.close()