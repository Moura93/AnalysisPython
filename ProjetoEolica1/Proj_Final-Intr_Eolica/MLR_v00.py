import pandas as pd
import numpy as np
import math
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

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

# ---- : : Versão 0.0 pela função split do scikitlearn : : ----

test_div = 0.5
rand = 0
# -- ML 128 --
y128 = df_merge['Vel (Mod)']
X128 = df_merge[['P2-128','P1-128','P3-128','P4-128']]

X128_train, X128_test, y128_train, y128_test = train_test_split(X128, y128, test_size=test_div, random_state=rand)

modelo128 = LinearRegression()
modelo128.fit(X128_train, y128_train)

y128_previsto = modelo128.predict(X128_test)

# -- ML 129 --
y129 = df_merge['Vel (Mod)']
X129 = df_merge[['P2-129','P1-129','P3-129','P4-129']]

X129_train, X129_test, y129_train, y129_test = train_test_split(X129, y129, test_size=test_div, random_state=rand)

modelo129 = LinearRegression()
modelo129.fit(X129_train, y129_train)

y129_previsto = modelo129.predict(X129_test)

# -- ML 130 --
y130 = df_merge['Vel (Mod)']
X130 = df_merge[['P2-130','P1-130','P3-130','P4-130']]

X130_train, X130_test, y130_train, y130_test = train_test_split(X130, y130, test_size=test_div, random_state=rand)

modelo130 = LinearRegression()
modelo130.fit(X130_train, y130_train)

y130_previsto = modelo130.predict(X130_test)

# -- ML 131 --
y131 = df_merge['Vel (Mod)']
X131 = df_merge[['P2-131','P1-131','P3-131','P4-131']]

X131_train, X131_test, y131_train, y131_test = train_test_split(X131, y131, test_size=test_div, random_state=rand)

modelo131 = LinearRegression()
modelo131.fit(X131_train, y131_train)

y131_previsto = modelo131.predict(X131_test)

# -- ML 132 --
y132 = df_merge['Vel (Mod)']
X132 = df_merge[['P2-132','P1-132','P3-132','P4-132']]

X132_train, X132_test, y132_train, y132_test = train_test_split(X132, y132, test_size=test_div, random_state=rand)

modelo132 = LinearRegression()
modelo132.fit(X132_train, y132_train)

y132_previsto = modelo132.predict(X132_test)

# -- ML 133 --
y133 = df_merge['Vel (Mod)']
X133 = df_merge[['P2-133','P1-133','P3-133','P4-133']]

X133_train, X133_test, y133_train, y133_test = train_test_split(X133, y133, test_size=test_div, random_state=rand)

modelo133 = LinearRegression()
modelo133.fit(X133_train, y133_train)

y133_previsto = modelo133.predict(X133_test)

# -- ML 134 --
y134 = df_merge['Vel (Mod)']
X134 = df_merge[['P2-134','P1-134','P3-134','P4-134']]

X134_train, X134_test, y134_train, y134_test = train_test_split(X134, y134, test_size=test_div, random_state=rand)

modelo134 = LinearRegression()
modelo134.fit(X134_train, y134_train)

y134_previsto = modelo134.predict(X134_test)

# -- ML 135 --
y135 = df_merge['Vel (Mod)']
X135 = df_merge[['P2-135','P1-135','P3-135','P4-135']]

X135_train, X135_test, y135_train, y135_test = train_test_split(X135, y135, test_size=test_div, random_state=rand)

modelo135 = LinearRegression()
modelo135.fit(X135_train, y135_train)

y135_previsto = modelo135.predict(X135_test)

# -- ML 136 --
y136 = df_merge['Vel (Mod)']
X136 = df_merge[['P2-136','P1-136','P3-136','P4-136']]

X136_train, X136_test, y136_train, y136_test = train_test_split(X136, y136, test_size=test_div, random_state=rand)

modelo136 = LinearRegression()
modelo136.fit(X136_train, y136_train)

y136_previsto = modelo136.predict(X136_test)

# -- ML 137 --
y137 = df_merge['Vel (Mod)']
X137 = df_merge[['P2-137','P1-137','P3-137','P4-137']]

X137_train, X137_test, y137_train, y137_test = train_test_split(X137, y137, test_size=test_div, random_state=rand)

modelo137 = LinearRegression()
modelo137.fit(X137_train, y137_train)

y137_previsto = modelo137.predict(X137_test)



print("ML 128")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo128.score(X128_train, y128_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo128.score(X128_train, y128_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y128_test, y128_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y128_test, y128_previsto)).round(5)))
print("Multiplicadores: ", modelo128.coef_)
print("Inter: ", modelo128.intercept_)
print("")
print("ML 129")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo129.score(X129_train, y129_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo129.score(X129_train, y129_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y129_test, y129_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y129_test, y129_previsto)).round(5)))
print("Multiplicadores: ", modelo129.coef_)
print("Inter: ", modelo129.intercept_)
print("")
print("ML 130")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo130.score(X130_train, y130_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo130.score(X130_train, y130_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y130_test, y130_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y130_test, y130_previsto)).round(5)))
print("Multiplicadores: ", modelo130.coef_)
print("Inter: ", modelo130.intercept_)
print("")
print("ML 131")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo131.score(X131_train, y131_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo131.score(X131_train, y131_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y131_test, y131_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y131_test, y131_previsto)).round(5)))
print("Multiplicadores: ", modelo131.coef_)
print("Inter: ", modelo131.intercept_)
print("")
print("ML 132")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo132.score(X132_train, y132_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo132.score(X132_train, y132_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y132_test, y132_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y132_test, y132_previsto)).round(5)))
print("Multiplicadores: ", modelo132.coef_)
print("Inter: ", modelo132.intercept_)
print("")
print("ML 133")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo133.score(X133_train, y133_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo133.score(X133_train, y133_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y133_test, y133_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y133_test, y133_previsto)).round(5)))
print("Multiplicadores: ", modelo133.coef_)
print("Inter: ", modelo133.intercept_)
print("")
print("ML 134")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo134.score(X134_train, y134_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo134.score(X134_train, y134_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y134_test, y134_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y134_test, y134_previsto)).round(5)))
print("Multiplicadores: ", modelo134.coef_)
print("Inter: ", modelo134.intercept_)
print("")
print("ML 135")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo135.score(X135_train, y135_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo135.score(X135_train, y135_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y135_test, y135_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y135_test, y135_previsto)).round(5)))
print("Multiplicadores: ", modelo135.coef_)
print("Inter: ", modelo135.intercept_)
print("")
print("ML 136")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo136.score(X136_train, y136_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo136.score(X136_train, y136_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y136_test, y136_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y136_test, y136_previsto)).round(5)))
print("Multiplicadores: ", modelo136.coef_)
print("Inter: ", modelo136.intercept_)
print("")
print("ML 137")
print("Coeficiênte de Determinação")
print("R² = {}".format(modelo137.score(X137_train, y137_train).round(5)))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(modelo137.score(X137_train, y137_train)).round(5)))
print("Coeficiênte de Determinação para as Previsões dos Modelos")
print("R² = %s" % metrics.r2_score(y137_test, y137_previsto).round(5))
print("Coeficiênte de Correlação de Pearson")
print("ρ = {}".format(np.sqrt(metrics.r2_score(y137_test, y137_previsto)).round(5)))
print("Multiplicadores: ", modelo137.coef_)
print("Inter: ", modelo137.intercept_)