import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_excel(r'era5.xlsx')
df['Vel'] = np.sqrt((df['u']**2)+(df['v']**2))

# Hodrick-Prescott Filter
paracuru_cycle, paracuru_trend = sm.tsa.filters.hpfilter(df['Vel'], lamb=1600)

plt.plot(paracuru_trend)
plt.show()
print(df)
