import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

df = pd.read_csv(r'PARACURU.csv', sep=",") #LEITURA DOS DADOS
df['DataTime'] = pd.to_datetime(df['DataTime']) #CONVERT TO DATETIME
# SELECT PERIOD
#df = df.loc[(df['DataTime'].dt.year==2005) & (df['DataTime'].dt.month==1)]
# Set the 'date' column as the index
df.set_index('DataTime', inplace=True)
# Resample the data to daily frequency and take the mean
#daily_average = df.resample('D').mean()
# Hodrick-Prescott Filter
paracuru_cycle, paracuru_trend = sm.tsa.filters.hpfilter(df['Vel (Mod)'], lamb=99999999)
# Plot
print(df)
plt.plot(df['Vel (Mod)'], '.', color='yellow')
plt.plot(paracuru_trend)
plt.show()
